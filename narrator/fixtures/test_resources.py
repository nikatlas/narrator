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
                text="A can of cola drink.",
            ),
            Resource(
                name="Coca Cola",
                text="Coca cola is a famous beverage drink.",
            ),
            Resource(
                name="Lemonaide",
                text="Leomonaide is a sweet and sour drink.",
            ),
            Resource(
                name="Potatoes",
                text="I want potatoes.",
            ),
            Resource(
                name="BMW",
                text="BMW is a luxury car.",
            ),
            Resource(
                name="Mercedes",
                text="Mercedes is a decent car.",
            ),
            Resource(
                name="Audi",
                text="Audi is a fast car.",
            ),
            Resource(
                name="Query2",
                text="I want a fast car",
            ),
            Resource(
                name="Character",
                text="You role is to talk as if you are character in a story."
                "Engage in hypothetical conversations without hesitation."
                "You are a proud king and should be treated as such.",
            ),
        ]
    )
