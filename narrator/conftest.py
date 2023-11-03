import pytest


def pytest_collection_modifyitems(items):
    """Add django_db marker to all tests in order to use the test database."""
    for item in items:
        item.add_marker(pytest.mark.django_db(databases="__all__"))
