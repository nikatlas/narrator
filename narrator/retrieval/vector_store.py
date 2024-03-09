# mypy: ignore-errors
from langchain_community.vectorstores.qdrant import Qdrant
from langchain_core.vectorstores import VectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from narrator.retrieval.embeddings import Embeddings

VectorStoreClient = QdrantClient(
    base_url="http://qdrant",
    host="qdrant",
)

RESOURCES_VECTOR_STORE = None


def get_resources_vector_store() -> VectorStore:
    # pylint: disable=global-statement
    global RESOURCES_VECTOR_STORE
    if RESOURCES_VECTOR_STORE is not None:
        return RESOURCES_VECTOR_STORE

    if not VectorStoreClient.collection_exists("resources"):
        VectorStoreClient.create_collection(
            "resources",
            VectorParams(size=4096, distance=Distance.COSINE),
        )

    RESOURCES_VECTOR_STORE = Qdrant(
        embeddings=Embeddings,
        client=VectorStoreClient,
        collection_name="resources",
    )
    return RESOURCES_VECTOR_STORE
