from langchain_community.chat_models import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from config import OpenAiCreds
from src.prompt import retrieval_qa_chat_prompt

def form_retrieval_chain(retriever=None):

    llm = ChatOpenAI(api_key=OpenAiCreds.API_KEY)
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return retrieval_chain
