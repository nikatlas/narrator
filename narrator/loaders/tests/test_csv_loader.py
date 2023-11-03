import pytest

from ..csv_loader import CSVLoader


def test_csv_loader():
    """Test CSVLoader"""
    loader = CSVLoader(filepath="loaders/tests/dummy_proposals.csv")
    loader.load()
    assert len(loader.data) == 50
    assert loader.data[0]["client_name"] == "ABB Asea Brown Boveri Ltd"

    with pytest.raises(IndexError):
        loader = CSVLoader(filepath="loaders/tests/dummy_proposals_broken.csv")
        loader.load()
