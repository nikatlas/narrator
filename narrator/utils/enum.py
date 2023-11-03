from typing import List

from enum import Enum as BaseEnum

from psqlextra.types import StrEnum as BaseStrEnum


class Enum(BaseEnum):
    """Extends the base enum class with some useful methods."""

    @classmethod
    def all(cls) -> List["Enum"]:
        return [choice for choice in cls]  # pylint: disable=unnecessary-comprehension

    @classmethod
    def values(cls) -> List[int]:
        return [choice.value for choice in cls]


class StrEnum(BaseStrEnum):
    """String Enum class"""
