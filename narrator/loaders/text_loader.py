from typing import Any, List, Optional

from os import path

from narrator.constants import PROJECT_DIR

from .loader import IDENTIFIER, Loader


class TextLoader(Loader):
    """
    Text data loader

    Parameters
    ----------
    filepath : str
        Filepath from which a text will be loaded
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.text: Optional[str] = None

    def load(self):
        with open(path.join(PROJECT_DIR, self.filepath), encoding="utf-8") as f:
            self.text = "\n".join(f.readlines())
        return self.text

    def list(self) -> Optional[List[Any]]:
        pass

    def get(self, key: IDENTIFIER) -> Optional[Any]:
        pass

    def search(self, query: Any) -> None:
        pass
