import os
from dotenv import load_dotenv

load_dotenv()

class OpenAiCreds:
    API_KEY = os.getenv("API_KEY", "")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "")

class GeneralParams:
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', ""))
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', ""))
    DATA_PATH = os.getenv('DATA_PATH', "")
    SEARCH_KWARGS = int(os.getenv('SEARCH_KWARGS', ""))
