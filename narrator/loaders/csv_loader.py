from typing import Any, List

import csv
from os import path

from narrator.constants import PROJECT_DIR

from .loader import IDENTIFIER, Loader


class CSVLoader(Loader):
    """
    CSV data loader

    Parameters
    ----------
    filepath : str
        Filepath from which a CSV will be loaded
    delimiter : str
        Delimiter that separates values from one column to another
    """

    def __init__(self, filepath: str, delimiter: str = ","):
        self.filepath = filepath
        self.delimiter = delimiter
        self.data: List[Any] = []

    def load(self) -> List[Any]:
        """Load data"""
        # Load csv file in memory
        with open(path.join(PROJECT_DIR, self.filepath), encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)

            # read headers
            headers = next(reader, None)
            if not headers:
                return []

            self.data.clear()
            for row in reader:
                if len(headers) != len(row):
                    raise IndexError(
                        "Number of columns does not match number of headers", row
                    )
                row_data = {}
                for index, _ in enumerate(headers):
                    row_data[headers[index]] = row[index]
                self.data.append(row_data)
        return self.data

    def list(self):
        pass

    def get(self, key: IDENTIFIER) -> None:
        pass

    def search(self, query: Any) -> None:
        pass
