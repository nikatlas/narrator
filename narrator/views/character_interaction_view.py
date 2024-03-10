from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from narrator.models import Character, CharacterInteraction, CharacterThread
from narrator.pipeline import PipelineContext
from narrator.pipelines.thread_conversation_pipeline import ThreadConversationPipeline
from narrator.serializers import CharacterInteractionSerializer


class CharacterInteractionViewSet(viewsets.ModelViewSet):
    queryset = CharacterInteraction.objects.all()
    serializer_class = CharacterInteractionSerializer

    @action(
        detail=False,
        methods=["get"],
        url_path=r"conversation/(?P<player_id>[^/]+)/(?P<npc_id>[^/]+)",
    )
    def conversation(self, request, player_id, npc_id):
        interactions = Character.get_interactions(player_id, npc_id)
        interactions_serialized = CharacterInteractionSerializer(
            interactions, many=True, context={"request": request}
        )
        return Response(interactions_serialized.data)

    @action(
        detail=False,
        methods=["post"],
        url_path=r"interact/(?P<player_id>[^/]+)/(?P<npc_id>[^/]+)",
    )
    @csrf_exempt
    @permission_classes([AllowAny])
    def interact(self, request, player_id, npc_id):
        message = request.data.get("message")
        if not message:
            return Response(
                {"error": "You must provide a message"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        payload = {
            "transmitter_character": player_id,
            "recipient_character": npc_id,
            "message": message,
        }
        context = PipelineContext(payload=payload)
        conversation_pipeline = ThreadConversationPipeline(context=context)
        conversation_pipeline.run()

        interactions = Character.get_interactions(player_id, npc_id)
        interactions_serialized = CharacterInteractionSerializer(
            interactions, many=True, context={"request": request}
        )
        return Response(interactions_serialized.data)

    @action(
        detail=False,
        methods=["delete"],
        url_path=r"interact/(?P<player_id>[^/]+)/(?P<npc_id>[^/]+)/clear",
    )
    @csrf_exempt
    @permission_classes([AllowAny])
    def clear_interactions(self, request, player_id, npc_id):

        try:
            CharacterInteraction.objects.filter(
                transmitter_character_id=player_id, recipient_character_id=npc_id
            ).delete()
            CharacterInteraction.objects.filter(
                transmitter_character_id=npc_id, recipient_character_id=player_id
            ).delete()
            threads = CharacterThread.objects.filter(
                transmitter_character_id=player_id, recipient_character_id=npc_id
            )
            for thread in threads:
                ThreadConversationPipeline.delete_thread(thread.thread_id)
            threads.delete()
        except CharacterThread.DoesNotExist:
            Response({"status": "not-found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"status": "ok"}, status=status.HTTP_204_NO_CONTENT)
