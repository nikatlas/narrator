from narrator.modules.chat_gpt_module import ChatGptModule
from narrator.pipeline.pipeline import Pipeline
from narrator.pipeline.pipeline_context import PipelineContext


class ConversationPipeline(Pipeline):
    """
    A pipeline for summarizing company content.
    This pipeline is designed to automatically generate concise summaries of
    company web content centered around important domain keywords using ChatGpt.

    @param context:Dict[str, Any] - contains input payload with a companies name,
    domain and keyword
    @return: str - summary
    """

    def __init__(
        self,
        context: PipelineContext,
    ):
        super().__init__(
            context,
            [
                ChatGptModule(),
            ],
        )

    # TODO: enable this to generate conversation context based on the characters
    # def pre_process(self, context: PipelineContext) -> Any:
    #     transmitter_character_pk = context.search_field("transmitter_character")
    #     recipient_character_pk = context.search_field("recipient_character")
    #
    #     transmitter = Character.objects.get(pk=transmitter_character_pk)
    #     recipient = Character.objects.get(pk=recipient_character_pk)
    #
    #     # make these serialisable
    #     interactions = recipient.get_interactions(transmitter)
    #     resources = recipient.get_resources()
    #
    #     return context
