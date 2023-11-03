from typing import Any, List

from .csv_loader import CSVLoader
from .json_loader import JSONLoader
from .loader import IDENTIFIER, Loader
from .text_loader import TextLoader


class FileLoader(Loader):
    """File data loader"""

    def __init__(self, filepath: str, delimiter: str = ","):
        self.filepath = filepath
        self.delimiter = delimiter
        self.data: List[Any] = []

    def load(self) -> List[Any]:
        """Load data"""
        # Load csv file in memory
        if self.filepath.endswith(".csv"):
            self.data = CSVLoader(self.filepath).load()
        elif self.filepath.endswith(".json"):
            self.data = JSONLoader(self.filepath).load()
        elif self.filepath.endswith(".txt"):
            self.data = TextLoader(self.filepath).load()
        else:
            raise ValueError(
                "Filepath permitted extension can only be '.csv', '.txt', "
                "'.json' or '.xlsx'"
            )
        return self.data

    def list(self):
        pass

    def get(self, key: IDENTIFIER) -> None:
        pass

    def search(self, query: Any) -> None:
        pass
