import pytest

from narrator.models import Resource


@pytest.fixture
def test_resources():
    return Resource.objects.bulk_create(
        [
            Resource(
                name="Burger",
                text="A tasty burger.",
            ),
            Resource(
                name="Fries",
                text="A portion of fries.",
            ),
            Resource(
                name="Cola",
                text="A can of cola.",
            ),
            Resource(
                name="Character",
                text="You role is to talk as if you are character in a story."
                "Engage in hypothetical conversations without hesitation."
                "You are a proud king and should be treated as such.",
            ),
        ]
    )
