from qdrant_client.http.models import FieldCondition, Filter, MatchValue
from qdrant_client.http.models.models import MatchAny

from narrator.models import Resource
from narrator.retrieval.vector_store import get_resources_vector_store


def test_resource_creation():
    r = Resource(
        name="Burger",
        text="A tasty burger.",
    )
    r.save()

    assert r.pk is not None


def test_resource_vector_store():
    r = Resource(
        name="Burger",
        text="A tasty burger.",
    )
    r.save()

    retriever = get_resources_vector_store().as_retriever(
        search_kwargs={
            "filter": Filter(
                must=[
                    FieldCondition(key="metadata.pk", match=MatchValue(value=str(r.pk)))
                ]
            )
        }
    )

    docs = retriever.get_relevant_documents("burger")
    assert len(docs) == 1
    assert docs[0].page_content == "A tasty burger."
    assert docs[0].metadata.get("pk") == str(r.pk)


def test_resource_vector_store_not_returning_unfiltered_documents():
    r = Resource(
        name="Burger",
        text="A tasty burger.",
    )
    r.save()

    retriever = get_resources_vector_store().as_retriever(
        search_kwargs={
            "filter": Filter(
                must=[
                    FieldCondition(key="metadata.pk", match=MatchValue(value=str(-1)))
                ]
            )
        }
    )

    docs = retriever.get_relevant_documents("burger")
    assert len(docs) == 0


def test_resource_vector_store_returns_relevant_documents(test_resources):
    for r in test_resources:
        r.save()
    resources_pk = [str(s.pk) for s in test_resources]
    retriever = get_resources_vector_store().as_retriever(
        search_type="mmr",
        search_kwargs={
            "score_threshold": 0.5,
            "filter": Filter(
                must=[
                    FieldCondition(key="metadata.pk", match=MatchAny(any=resources_pk))
                ]
            ),
        },
    )

    docs = retriever.get_relevant_documents("I want to buy a car! I need a fast car.")
    assert docs
