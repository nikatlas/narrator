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
