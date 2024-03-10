from django.conf import settings
from langchain_community.embeddings import OllamaEmbeddings

OLLAMA_HOST = settings.OLLAMA_HOST
OLLAMA_PORT = settings.OLLAMA_PORT

Embeddings = OllamaEmbeddings(
    model="mistral", base_url=f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"
)
