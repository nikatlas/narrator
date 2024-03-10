from django.conf import settings
from langchain_community.embeddings import HuggingFaceEmbeddings  # , OllamaEmbeddings

OLLAMA_HOST = settings.OLLAMA_HOST
OLLAMA_PORT = settings.OLLAMA_PORT

# Embeddings = OllamaEmbeddings(
#     model="mistral", base_url=f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"
# )
Embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
print("Embeddings loaded!")
