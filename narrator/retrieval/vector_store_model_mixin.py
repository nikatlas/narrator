from typing import Optional

from abc import abstractmethod

from langchain.indexes import index
from langchain.indexes.base import RecordManager
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter


class VectorStoreModelMixin:
    def __init__(  # type: ignore
        self,
        *args,
        text_splitter: Optional[TextSplitter] = None,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.text_splitter = text_splitter or RecursiveCharacterTextSplitter()

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

    @classmethod
    @abstractmethod
    def get_vector_store(cls) -> VectorStore:
        pass

    @classmethod
    @abstractmethod
    def get_vector_store_record_manager(cls) -> RecordManager:
        pass

    def save(self, *args, **kwargs):
        super_save = getattr(super(), "save")
        if super_save and callable(super_save):
            super_save(*args, **kwargs)

        documents = self.to_documents()
        chunked_documents = self.split_documents(documents)
        index(
            chunked_documents,
            self.get_vector_store_record_manager(),
            self.get_vector_store(),
            cleanup="incremental",
            source_id_key=self.get_document_object_id_field(),
        )
