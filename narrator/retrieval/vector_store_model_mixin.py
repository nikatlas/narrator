from typing import Optional

from abc import abstractmethod

from django.contrib.postgres.fields import ArrayField
from django.db import models
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.qdrant import Qdrant
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter


class VectorStoreModelMixin:
    class Meta:
        vector_store_collection_name = "default"

    document_ids = ArrayField(models.IntegerField())

    def __init__(  # type: ignore
        self,
        *args,
        vector_store: Optional[VectorStore] = None,
        embeddings_model: Optional[OllamaEmbeddings] = None,
        text_splitter: Optional[TextSplitter] = None,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.text_splitter = text_splitter or RecursiveCharacterTextSplitter()
        self.embeddings_model = embeddings_model or OllamaEmbeddings(model="mistral")
        self.vector_store: VectorStore = vector_store or Qdrant(
            embeddings=self.embeddings_model,
            client="http://localhost:6333",
            collection_name=getattr(self, "_meta").vector_store_collection_name
            or "default",
        )

    def set_vector_store(self, vector_store):
        self.vector_store = vector_store

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)

    @abstractmethod
    def to_documents(self) -> list[Document]:
        pass

    def save(self, *args, **kwargs):
        documents = self.to_documents()
        splitted_documents = self.split_documents(documents)

        # store the vectors
        self.vector_store.add_documents(splitted_documents)
        super_test = getattr(super(), "save")
        if super_test and callable(super_test):
            super_test().save(*args, **kwargs)
