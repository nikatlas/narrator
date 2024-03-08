from typing import Optional

from abc import abstractmethod

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.qdrant import Qdrant
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter
from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    VectorParams,
)


class VectorStoreModelMixin:
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
        self.embeddings_model = embeddings_model or OllamaEmbeddings(
            model="mistral", base_url="http://ollama:11434"
        )
        self.vector_store_client = QdrantClient(
            base_url="http://qdrant",
            host="qdrant",
        )
        self.vector_store: VectorStore = vector_store or Qdrant(
            embeddings=self.embeddings_model,
            client=self.vector_store_client,
            collection_name=self.get_vector_store_collection_name(),
        )

    def set_vector_store(self, vector_store):
        self.vector_store = vector_store

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)

    @abstractmethod
    def to_documents(self) -> list[Document]:
        pass

    @abstractmethod
    def get_vector_store_collection_name(self) -> str:
        pass

    @abstractmethod
    def get_document_object_id_field(self) -> str:
        pass

    def save(self, *args, **kwargs):
        super_save = getattr(super(), "save")
        if super_save and callable(super_save):
            super_save(*args, **kwargs)

        documents = self.to_documents()
        splitted_documents = self.split_documents(documents)

        if not self.vector_store_client.collection_exists(
            self.get_vector_store_collection_name()
        ):
            self.vector_store_client.create_collection(
                self.get_vector_store_collection_name(),
                VectorParams(size=4096, distance=Distance.COSINE),
            )

        object_id = getattr(self, self.get_document_object_id_field())
        # store the vectors
        matches, _ = self.vector_store_client.scroll(
            collection_name=self.get_vector_store_collection_name(),
            scroll_filter=Filter(
                must=[
                    FieldCondition(
                        key=f"metadata.{self.get_document_object_id_field()}",
                        match=MatchValue(value=object_id),
                    )
                ]
            ),
        )
        if matches:
            self.vector_store.delete(ids=[str(match.id) for match in matches])
        self.vector_store.add_documents(splitted_documents)
