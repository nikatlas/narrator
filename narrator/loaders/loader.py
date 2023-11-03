from typing import Any

from abc import ABC, abstractmethod

IDENTIFIER = int


class Loader(ABC):
    """Abstract class for data loaders"""

    @abstractmethod
    def load(self):
        """Load data"""

    @abstractmethod
    def list(self):
        """List data"""

    @abstractmethod
    def get(self, key: IDENTIFIER) -> None:
        """Get data"""

    @abstractmethod
    def search(self, query: Any) -> None:
        """Search data"""
