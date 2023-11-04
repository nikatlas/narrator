def test_character_get_interactions(test_characters):
    """Test character get interactions."""
    character = test_characters[0]
    other_character = test_characters[1]

    interactions = character.get_interactions(other_character)

    assert interactions.count() == 3
    assert interactions[0].text == "Hello, how are you?"
    assert interactions[1].text == "I'm fine, thanks."
    assert interactions[2].text == "What do you mean you are fine?"

    other_character = test_characters[2]
    interactions = character.get_interactions(other_character)

    assert interactions.count() == 2
    assert interactions[0].text == "What are we gonna eat? I am hungry."
    assert interactions[1].text == "I don't know, maybe a burger?"

    other_interactions = other_character.get_interactions(character)
    assert other_interactions.count() == 2
    assert [i.pk for i in other_interactions] == [i.pk for i in interactions]


def test_character_get_context(test_characters, test_resources):
    test_characters[0].resources.add(test_resources[0])
    test_characters[0].resources.add(test_resources[1])

    context = test_characters[0].get_context(test_characters[1])

    assert context["interactions"][0]["role"] == "assistant"
    assert context["interactions"][0]["content"] == "Hello, how are you?"
    assert context["interactions"][1]["role"] == "user"
    assert context["interactions"][1]["content"] == "I'm fine, thanks."
    assert context["interactions"][2]["role"] == "assistant"
    assert context["interactions"][2]["content"] == "What do you mean you are fine?"
    assert len(context["interactions"]) == 3
    assert context["resources"][0]["role"] == "system"
    assert context["resources"][0]["content"] == "A tasty burger."
    assert context["resources"][1]["role"] == "system"
    assert context["resources"][1]["content"] == "A portion of fries."
    assert len(context["resources"]) == 2
