from django.db import models
from langchain_core.documents import Document

from narrator.retrieval.vector_store_model_mixin import VectorStoreModelMixin


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_documents(self):
        return [Document(self.text, metadata={"pk": self.pk, "name": self.name})]

    def get_vector_store_collection_name(self):
        return "resources"

    def get_document_object_id_field(self):
        return "pk"
