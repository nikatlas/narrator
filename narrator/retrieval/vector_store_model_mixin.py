from typing import Optional

from abc import abstractmethod

import structlog
from langchain.indexes import index
from langchain.indexes.base import RecordManager
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter

logger = structlog.getLogger(__name__)


class VectorStoreModelMixin:
    def __init__(  # type: ignore
        self,
        *args,
        text_splitter: Optional[TextSplitter] = None,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.text_splitter = text_splitter or RecursiveCharacterTextSplitter(
            chunk_size=400
        )

    def split_documents(self, documents):
        # # This text splitter is used to create the parent documents
        # parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
        # # This text splitter is used to create the child documents
        # # It should create documents smaller than the parent
        # child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
        # # The storage layer for the parent documents
        # store = InMemoryStore()
        # retriever = ParentDocumentRetriever(
        #     vectorstore=self.get_vector_store(),
        #     docstore=store,
        #     child_splitter=child_splitter,
        #     parent_splitter=parent_splitter,
        # )
        # retriever.add_documents(documents)
        # chunked_documents = store.mget(store.yield_keys())
        #
        # return chunked_documents
        return self.text_splitter.split_documents(documents)

    @abstractmethod
    def to_documents(self) -> list[Document]:
        pass

    @abstractmethod
    def add_metadata(self, document: Document) -> Document:
        return document

    @abstractmethod
    def get_vector_store_collection_name(self) -> str:
        pass

    @abstractmethod
    def get_document_object_id_field(self) -> str:
        """This is the `key` in the metadata that will be used to identify the document.

        It will be used to index the documents associated with this model to the
        VectorStore.
        Every document should have a unique value for this key per instance of the
        model, so that it will be properly updated and deleted when the model is updated
        or deleted.
        """

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
        documents_with_metadata = [
            self.add_metadata(document) for document in documents
        ]
        chunked_documents = self.split_documents(documents_with_metadata)
        indexing_results = index(
            chunked_documents,
            self.get_vector_store_record_manager(),
            self.get_vector_store(),
            cleanup="incremental",
            source_id_key=self.get_document_object_id_field(),
        )
        logger.info(
            f"Indexing results for "
            f"{getattr(self, self.get_document_object_id_field())}",
            results=indexing_results,
            documents=len(chunked_documents),
        )
