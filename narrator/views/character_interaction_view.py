from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from narrator.models import Character, CharacterInteraction
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
