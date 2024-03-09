# from bs4 import BeautifulSoup as Soup
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.vectorstores import Qdrant
# from langchain_community.document_loaders import RecursiveUrlLoader  # , WebBaseLoader
# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.llms import Ollama
#
# # from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_text_splitters import RecursiveCharacterTextSplitter
#
# print("Loading docs...")
# # loader = WebBaseLoader("https://tonersales.eu/shop")
# URL = "https://tonersales.eu/shop"
# loader = RecursiveUrlLoader(
#     url=URL, max_depth=1, extractor=lambda x: Soup(x, "html.parser").text
# )
# docs = loader.load()
# print(f"Loaded {len(docs)} docs")
# print(docs)
# embeddings = OllamaEmbeddings(model="mistral")
#
#
# text_splitter = RecursiveCharacterTextSplitter()
# documents = text_splitter.split_documents(docs)
# vector = Qdrant.from_documents(documents, embeddings)
#
#
# llm = Ollama(model="mistral")
#
# prompt = ChatPromptTemplate.from_template(
#     """
# Answer the following question based only on the provided context:
# <context>
# {context}
# </context>
#
# Question: {input}"""
# )
#
# document_chain = create_stuff_documents_chain(llm, prompt)
#
# retriever = vector.as_retriever()
# retrieval_chain = create_retrieval_chain(retriever, document_chain)
#
# chain = retrieval_chain
#
# prompt_text = "What is tonersales?"
# print(f"Prompting: {prompt_text}")
# r = chain.invoke({"input": prompt_text})
#
# print(r)
# print(r["answer"])
