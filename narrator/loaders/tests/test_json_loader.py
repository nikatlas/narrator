from typing import Any, Dict

import json
import os

import pytest

from ..json_loader import JSONLoader


def test_json_loader():
    """Test JSONLoader"""
    unexistent_filepath = "loaders/tests/a.json"
    if os.path.exists(os.path.join("narrator", unexistent_filepath)):
        os.remove(os.path.join("narrator", unexistent_filepath))

    loader = JSONLoader(filepath=unexistent_filepath)
    with pytest.raises(ValueError):
        loader.save()

    loader = JSONLoader(filepath=unexistent_filepath, data=[1, 2])
    loader.save()

    if os.path.exists(os.path.join("narrator", unexistent_filepath)):
        os.remove(os.path.join("narrator", unexistent_filepath))

    loader = JSONLoader(filepath="loaders/tests/dummy_json.json")
    loader.load()
    data: Dict[Any, Any] = dict(loader.data)
    assert data.get("a") == 1

    with pytest.raises(json.decoder.JSONDecodeError):
        loader = JSONLoader(filepath="loaders/tests/dummy_json_broken.json")
        loader.load()

    assert not loader.list()
