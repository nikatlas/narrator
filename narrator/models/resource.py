import structlog
from django.db import models
from langchain.indexes.base import RecordManager
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore

from narrator.retrieval.index import get_resources_record_manager
from narrator.retrieval.vector_store import get_resources_vector_store
from narrator.retrieval.vector_store_model_mixin import VectorStoreModelMixin

logger = structlog.getLogger(__name__)


class Resource(VectorStoreModelMixin, models.Model):
    """Resource model.

    Resources are pieces of information that can be attached to characters.
    They can be used to provide additional information about a character,
    give world context and more.
    """

    class Meta:
        """Meta class."""

        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    name = models.CharField(max_length=255)
    text = models.TextField()
    file = models.FileField(upload_to="uploads", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_documents(self):
        documents = [
            Document(self.text, metadata={"pk": str(self.pk), "name": self.name})
        ]
        if self.file:
            try:
                loader = PyPDFLoader(self.file.name)
                pages = loader.load()
                documents.extend(pages)
            except Exception as exc:  # pylint: disable=broad-except
                logger.error("Error loading PDF", error=exc)
        return documents

    def add_metadata(self, document):
        document.metadata["pk"] = str(self.pk)
        document.metadata["name"] = self.name
        return document

    def get_vector_store_collection_name(self):
        return "resources"

    def get_document_object_id_field(self):
        return "pk"

    @classmethod
    def get_vector_store(cls) -> VectorStore:
        return get_resources_vector_store()

    @classmethod
    def get_vector_store_record_manager(cls) -> RecordManager:
        return get_resources_record_manager()
