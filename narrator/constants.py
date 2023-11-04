from os import environ, path

PROJECT_DIR = path.dirname(path.abspath(__file__))
DATABASE_DIR = path.join(PROJECT_DIR, "../databases")

AZURE_SPEECH_KEY = environ.get("AZURE_SPEECH_KEY", "5738c9014fc04c459a6e20091a7117fc")
AZURE_SPEECH_REGION = environ.get("AZURE_SPEECH_REGION", "westeurope")


OPENAI_API_ENDPOINT = environ.get("OPENAI_API_ENDPOINT", "https://api.openai.com/v1")
OPENAI_API_TYPE = environ.get("OPENAI_API_TYPE", "openai")
OPENAI_API_KEY = environ.get(
    "OPENAI_API_KEY", "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"
)
OPEN_AI_VERSION = environ.get("OPENAI_API_VERSION", "")
