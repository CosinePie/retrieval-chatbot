from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import OpenAiCreds

def create_vector_db(documents=None):

    embedding_model = OpenAIEmbeddings(openai_api_key=OpenAiCreds.API_KEY, model=OpenAiCreds.EMBEDDING_MODEL)
    db = FAISS.from_documents(documents, embedding_model)
    retriever = db.as_retriever()
    
    return retriever
