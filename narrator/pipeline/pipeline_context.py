from typing import Any, Dict, List, Optional

import copy
from dataclasses import dataclass

from narrator.utils import Enum

UNSPECIFIED = object()


class ExecutionStatus(Enum):
    """Execution status of a module."""

    SUCCESS = 0
    FAILURE = 1
    SKIPPED = 2


@dataclass
class ExecutionState:
    """
    Execution state of a module.
    This dataclass contains the context, error and status after
    a module is executed.
    """

    context: "PipelineContext"
    error: Optional[Exception]
    status: ExecutionStatus


class PipelineContext:
    """
    Interface for pipeline contexts.

    Pipeline contexts are shared memory between the modules in a pipeline.
    This is useful for storing intermediate results or metadata.
    """

    _payload: Any
    _result: Any
    _data: Dict[str, Any]
    states: List[ExecutionState]

    def __init__(self, payload: Any):
        """
        Initializes the pipeline context with the given payload.

        Parameters
        ----------
        payload : Any
            The payload of the context.
            Should be processable by the first module in the pipeline.
        """
        self._payload = payload
        self._result = None
        self._data = {}
        self.states = []

    def add(self, key: str, value: Any) -> "PipelineContext":
        """
        Adds a key-value pair to the context.
        :param key: str
        :param value: Any
        """
        if key in self._data:
            raise SyntaxError(
                "You cannot set an already existing key in the 'context' with"
                "the add() method, you have to use the update() method for changes."
            )
        self._data[key] = value

        return self

    def update(self, key: str, new_value: Any) -> Any:
        """
        Updates by completely overriding the existing content stored a in a key with a
        new value.
        :param key: str
        :param value: Any
        """
        if key not in self._data:
            raise SyntaxError(
                "You cannot update a key in the '_data' if it does not exist."
            )
        self._data[key] = new_value

        return self._data[key]

    def merge(self, key: str, new_value: Any, remove_duplicates: bool = False) -> Any:
        """
        Updates by merging the existing content stored a in a key with a new value.
        :param key: str
        :param new_value: Any
        :param remove_duplicates: bool
        """
        if key not in self._data:
            self._data[key] = new_value
            return self._data[key]

        value = self._data[key]
        if isinstance(value, dict):
            value.update(new_value)
        elif isinstance(value, (list, str)):
            value += new_value
        elif isinstance(value, set):
            value |= new_value
        else:
            raise TypeError(f"New type with unhandled merge operation: {type(value)}!")

        if remove_duplicates:
            if isinstance(value, list):
                value = list(set(value))

        self._data[key] = value

        return self._data[key]

    def exists_field(self, key: str) -> bool:
        return key in self._data

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Returns the value for the given key.
        :param key: str
        :param default: Any
            default value to be returned if key is not found in the context
        :return:
        """
        return self._data.get(key, default)

    def delete(self, key: str) -> Any:
        """
        Deletes an entry for a given key and returns it
        :param key: str
        :return:
        """
        return self._data.pop(key)

    def submit_module_execution(self, execution_state: ExecutionState) -> None:
        """
        When a module is executed on top of this context, the action is logged
        along with the results.
        This method is to be called by the Pipeline itself.

        :param execution_state: Module
        """
        self.states.append(execution_state)

    def get_last_module_execution(self) -> Optional[ExecutionState]:
        """
        Returns the last module execution.
        :return: Module
        """
        return self.states[-1] if self.states else None

    def clone(self, new_payload: Optional[Any] = None) -> "PipelineContext":
        cloned_context = copy.deepcopy(self)
        # Persist references to the original context inside the state property
        cloned_context.states = self.states.copy()
        if new_payload:
            cloned_context._payload = new_payload  # pylint: disable=protected-access
        return cloned_context

    def search_field(self, field: Any, default: Optional[Any] = UNSPECIFIED) -> Any:
        """
        Searches a field first in the payload, then as a fallback mechanism it tries
        to search it in the data attribute, if it is not present there either it
        retrieves default if the default is available, if not it will raise an error.
        :param field: Any
        :param default: Any
        :return:
        """
        if isinstance(self.payload, Dict) and field in self.payload:
            return self.payload[field]

        value = self.get(field)
        if value is not None:
            return value

        if default is UNSPECIFIED:
            raise ValueError(
                f"Could not find `{field}` and no "
                "value was provided for the field 'default'!"
            )

        return default

    #############################
    # Getters and Setters
    #############################

    @property
    def payload(self) -> Any:
        """
        Returns the payload of the context.
        """
        return self._payload

    @payload.setter
    def payload(self, _: Any) -> None:
        """
        You cannot set the payload of the context.
        You can make a new context with the payload you want.
        """

        raise SyntaxError(
            "You cannot set the payload of the context. You can make a new context"
            + "with the payload you want."
        )

    @property
    def result(self) -> Any:
        """
        Returns the result of the context.
        """
        return self._result

    @result.setter
    def result(self, _: Any) -> None:
        """
        You should not set the result of the context.
        The result is set by the Pipeline when a module execution is completed.
        """
        raise SyntaxError(
            "You should not set the result of the context. The result is set by "
            + "the Pipeline when a module execution is completed."
        )
