from typing import Any, Dict

from narrator.chatgpt.chat_gpt import ChatGpt
from narrator.pipeline import PipelineContext, PipelineModule

Input = Dict[str, Any]
Output = str


class ChatGptModule(PipelineModule[Input, Output]):
    """Class for instantiating ChatGpt object

    This module is designed to make chatGPT requests and generate the outputs.
    Metadata context variables below are used to adjust the GPT model:

    num_words: int - max words requested by query
    engine: Literal["gpt3.5", "gpt4"] - what gpt to use
    temperature: float - adjust GPT creativity
    max_tokens: int - max words in response
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    """

    def __init__(
        self,
        name: str = "chat_gpt",
        **kwargs: Any,
    ):
        super().__init__(name, **kwargs)

    def run(self, context: PipelineContext) -> Output:
        """
        Function that runs the ChatGPT module

        @param context: Dict[str, Any] - it should contain company_name:str,
        keyword:str, num_words:int, web_content:str
        @return: output_messages: List[Dict[str, str]] - list of summaries
        """

        if not isinstance(context.payload, dict):
            raise ValueError("Payload should have been a dictionary")

        chat_gpt = ChatGpt()

        conversation = context.search_field("conversation", [])

        parameter_dict = chat_gpt.default_configuration()
        for parameter, value in parameter_dict.items():
            parameter_dict[parameter] = context.search_field(
                field=parameter, default=value
            )
        parameter_dict["messages"] = conversation
        response = chat_gpt.request(**parameter_dict)
        output_messages = chat_gpt.get_output_from_response(response)

        return str(output_messages[0]["content"])
