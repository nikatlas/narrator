import pytest

from ..file_loader import FileLoader


def test_file_loader():
    """Test FileLoader"""
    loader = FileLoader(filepath="loaders/tests/dummy_proposals.csv")
    loader.load()
    data_keys = sorted(
        [
            "client_name",
            "supplier_name",
            "proposal_status",
            "award_status",
            "create_date",
            "project_id",
            "project_name",
            "servicestandard",
            "project_location",
            "project_status",
            "seniority_standard",
            "seniority_level",
            "rate",
            "currency",
            "analysis_days",
            "concept_days",
            "implementation_days",
            "audit_days",
            "total_days",
            "proposal_id",
            "rate_total",
            "proposal_total",
            "supp_perc",
            "supp_total",
            "man_days",
        ]
    )
    assert len(loader.data) == 50
    assert isinstance(loader.data, list)
    assert isinstance(loader.data[0], dict)
    assert sorted(loader.data[0].keys()) == data_keys

    assert loader.data[0]["client_name"] == "ABB Asea Brown Boveri Ltd"

    with pytest.raises(IndexError):
        loader = FileLoader(filepath="loaders/tests/dummy_proposals_broken.csv")
        loader.load()

    with pytest.raises(ValueError):
        loader = FileLoader(filepath="loaders/tests/a.yml")
        loader.load()

    loader = FileLoader(filepath="loaders/tests/dummy_json.json")
    assert len(loader.load()) == 2

    loader = FileLoader(filepath="loaders/tests/a.txt")
    assert len(loader.load()) == 14
