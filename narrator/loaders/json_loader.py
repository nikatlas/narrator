from typing import Any, Dict, List, Optional, Union

import json
from os import path

from narrator.constants import PROJECT_DIR

from .loader import IDENTIFIER, Loader


class JSONLoader(Loader):
    """CSV data loader"""

    def __init__(
        self, filepath: str, data: Optional[Union[List[Any], Dict[Any, Any]]] = None
    ):
        self.filepath = path.join(PROJECT_DIR, filepath)
        self.data: Union[List[Any], Dict[Any, Any]] = data or []

    def load(self, new_filepath: str = "") -> Any:
        if new_filepath:
            self.filepath = new_filepath
        with open(self.filepath, encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data

    def save(self):
        if self.data:
            with (
                open(path.join(PROJECT_DIR, self.filepath), encoding="utf-8", mode="w")
            ) as f:
                json.dump(self.data, f, indent=4)
        else:
            raise ValueError("Cannot serialize data in a json when data is empty")

    def list(self) -> Optional[List[Any]]:
        if isinstance(self.data, list):
            return self.data
        return None

    def get(self, key: IDENTIFIER) -> Optional[Any]:
        if isinstance(self.data, dict):
            return self.data.get(key, None)
        return None

    def search(self, query: Any) -> None:
        pass
