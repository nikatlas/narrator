from typing import Callable, Generic, Optional, TypeVar

from abc import ABC, abstractmethod

from .pipeline_context import PipelineContext

Input = TypeVar("Input")
Output = TypeVar("Output")

PreProcess = Callable[[PipelineContext], Input]
PostProcess = Callable[[PipelineContext], Output]


class PipelineModule(ABC, Generic[Input, Output]):
    """
    Interface for creating modules.

    Modules are the building blocks of pipelines.
    They are the individual steps that are executed in order.
    Each module is responsible for processing the data in the context and
    :return the result back.
    """

    def __init__(
        self,
        name: str,
        pre_process: Optional[PreProcess[Input]] = None,
        post_process: Optional[PostProcess[Output]] = None,
    ):
        self.name = name
        self._pre_processor: Optional[PreProcess[Input]] = pre_process
        self._post_processor: Optional[PostProcess[Output]] = post_process

    def should_skip(
        self, context: PipelineContext  # pylint: disable=unused-argument
    ) -> bool:
        """
        Returns whether the module should be skipped.
        Each module that wants to implement a skip behaviour should override
        this method.

        @:param context: PipelineContext
            The shared memory between the modules.
        @:return bool: Whether the module should be skipped.
        """
        return self.name in context.search_field("skip", [])

    @abstractmethod
    def run(self, context: PipelineContext) -> Output:
        """
        Runs the module.

        @:param context : PipelineContext
            The shared memory between the modules.
        @:return PipelineContext
            The context after the module has finished.
        """

    def pre_process(self, context: PipelineContext) -> Input:
        """
        Runs before the module.

        @:param context : PipelineContext
            The context before the module has started.
        @:return processed_payload : Output
            The payload that the module will ingest.
            By default, it returns the payload from the context.
        """
        payload: Input = context.payload
        return self._pre_processor(context) if self._pre_processor else payload

    def post_process(self, context: PipelineContext) -> Output:
        """
        Runs after the module.

        @:param context : PipelineContext
            The context after the module has finished.
        @:param result : Output
            The output of the module.
            By default, it returns the result from the context.
        """
        result: Output = context.result
        return self._post_processor(context) if self._post_processor else result
