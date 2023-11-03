from ..text_loader import TextLoader


def test_text_loader():
    """Test TextLoader"""
    data = TextLoader(filepath="loaders/tests/a.txt").load()
    assert len(data) == 14
