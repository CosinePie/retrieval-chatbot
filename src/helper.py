from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import GeneralParams

def load_pdf(path):
    """
    Load PDF documents from the specified directory.

    Parameters:
    - path (str): The path to the directory containing PDF files.

    Returns:
    - List[Document]: A list of Document objects representing the loaded PDF files.
    """
    loader = DirectoryLoader(path=path, glob='*.pdf', loader_cls=PyPDFLoader, show_progress=True)
    docs = loader.load()
    return docs


def split_text(documents):
    """
    Split the text content of documents into chunks using a recursive character-based approach.

    Parameters:
    - documents (List[Document]): A list of Document objects containing text to be split.

    Returns:
    - List[str]: A list of text chunks obtained from splitting the input documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=GeneralParams.CHUNK_SIZE, chunk_overlap=GeneralParams.CHUNK_OVERLAP)
    text_chunks = text_splitter.split_documents(documents=documents)
    return text_chunks
