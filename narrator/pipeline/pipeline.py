from typing import Any, List, Optional

from .pipeline_context import ExecutionState, ExecutionStatus, PipelineContext
from .pipeline_module import PipelineModule


class PipelineError(Exception):
    """Raised when a Pipelines raise an error."""

    context: PipelineContext

    def __init__(self, message: str, context: PipelineContext):
        self.context = context
        super().__init__(message)


class Pipeline:
    """
    Interface for creating pipelines.

    Pipelines are a set of steps that are executed in order.
    They consist of Modules and a PipelineContext that is passed between them.
    Each pipeline run is accompanied by a context which works as a
    shared memory between the modules. This is useful for storing
    intermediate results or metadata.

    Parameters
    ----------
    context: PipelineContext
        Context of the pipeline which receives and passes along data across a
        pipeline enriching it with information from the modules provided below
    modules: Optional[List[PipelineModule[Any, Any]]] = None
        Define the running logic and behavior of the pipeline
    """

    _modules: List[PipelineModule[Any, Any]]
    _context: PipelineContext
    _execution_contexts: List[PipelineContext]

    def __init__(
        self,
        context: PipelineContext,
        modules: Optional[List[PipelineModule[Any, Any]]] = None,
    ):
        """
        Initializes the pipeline with the given modules and context.

        @:param context : dict
            The shared memory between the modules.
        @:param modules : Optional[List[Module]]
            The modules that will be executed in order.
        """
        self._context = context
        self._modules = modules or []
        self._execution_contexts = []

    def pre_process(self, context: PipelineContext) -> Any:
        """
        Performs a pre-processing before the pipeline is run.
        You can use the context and payload to modify the context.

        @:param context : PipelineContext
            The context that will be used to run the pipeline.
        """
        return context.payload

    def post_process(self, context: PipelineContext) -> Any:
        """
        Performs a post-processing after the pipeline is run.
        You can use the context, payload and result to return the result
        that is desired.

        @:param context : PipelineContext
            The context after running the pipeline.
        @:return Any
            The result of the post-processing, which will be the result of the whole
            pipeline. By default, it returns the result of the pipeline.
        """
        return context.result

    def add_module(
        self, module: PipelineModule[Any, Any], position: Optional[int] = None
    ) -> "Pipeline":
        """
        Adds a module to the pipeline.

        @:param module : Module
            The module to be added.
        @:param position : int, optional
            The position in the pipeline where the module will be added.
            If no position is given, the module will be added at the end.
        """
        if position is None:
            self._modules.append(module)
        else:
            self._modules.insert(position, module)

        return self

    def run(self) -> PipelineContext:
        """
        Runs the pipeline.

        @:return PipelineContext
            The context after the pipeline has finished.
        """
        # pylint: disable=protected-access
        context = self._context.clone()
        context._payload = self.pre_process(context)

        for module in self._modules:
            try:
                if module.should_skip(context):
                    state = ExecutionState(
                        context=context, error=None, status=ExecutionStatus.SKIPPED
                    )
                else:
                    context._payload = module.pre_process(context)
                    context._result = module.run(context)
                    context._result = module.post_process(context)
                    state = ExecutionState(
                        context=context, error=None, status=ExecutionStatus.SUCCESS
                    )
            except Exception as e:  # pylint: disable=broad-exception-caught
                state = ExecutionState(
                    context=context, error=e, status=ExecutionStatus.FAILURE
                )
                context.submit_module_execution(state)
                self._execution_contexts.append(context)
                raise PipelineError("Pipeline failure", context) from e

            context.submit_module_execution(state)
            self._execution_contexts.append(context)
            context = context.clone(context.result)

        # Re-attach the initial payload to the context so that it represents
        # the start to end state of the pipeline.
        context._payload = self._context.payload
        context._result = self.post_process(context)

        # pylint: enable=protected-access
        return context

    #############################
    # Getters and Setters
    #############################

    @property
    def modules(self) -> List[PipelineModule[Any, Any]]:
        """
        Returns the modules that are currently loaded in the pipeline.
        """
        return self._modules

    @modules.setter
    def modules(self, _):
        """
        You cannot set the modules of the pipeline.
        You can use add_module() to add a module to the pipeline.
        """

        raise SyntaxError(
            "You cannot set the modules of the pipeline."
            + "You can use add_module() to add a module to the pipeline."
        )

    @property
    def context(self) -> PipelineContext:
        """
        Returns the current state of the context.
        """
        return self._context

    @context.setter
    def context(self, _):
        """
        You cannot set the context of the pipeline.
        It is automatically set when the pipeline is initialized and modified
        when a module is executed.
        """

        raise SyntaxError(
            "You cannot set the context of the pipeline. It is automatically "
            + "set when the pipeline is initialized and modified when a module "
            + "is executed."
        )
