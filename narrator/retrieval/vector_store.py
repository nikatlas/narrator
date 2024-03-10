# mypy: ignore-errors
from django.conf import settings
from langchain_community.vectorstores.qdrant import Qdrant
from langchain_core.vectorstores import VectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from narrator.retrieval.embeddings import Embeddings

QDRANT_HOST = settings.QDRANT_HOST

VectorStoreClient = QdrantClient(
    base_url=f"http://{QDRANT_HOST}",
    host=QDRANT_HOST,
)

RESOURCES_VECTOR_STORE = None
RESOURCES_COLLECTION = "resources"


def get_resources_vector_store() -> VectorStore:
    # pylint: disable=global-statement
    global RESOURCES_VECTOR_STORE
    if RESOURCES_VECTOR_STORE is not None:
        return RESOURCES_VECTOR_STORE

    if not VectorStoreClient.collection_exists(RESOURCES_COLLECTION):
        VectorStoreClient.create_collection(
            RESOURCES_COLLECTION,
            VectorParams(size=4096, distance=Distance.COSINE),
        )

    RESOURCES_VECTOR_STORE = Qdrant(
        embeddings=Embeddings,
        client=VectorStoreClient,
        collection_name=RESOURCES_COLLECTION,
    )
    return RESOURCES_VECTOR_STORE
