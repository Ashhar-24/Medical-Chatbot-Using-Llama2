from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter      #for creating chunks
from langchain_community.embeddings import HuggingFaceEmbeddings

# Data extraction from pdf
def load_pdf(data):
    loader= DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents= loader.load()

    return documents


# Creating text Chunks so that the entire pdf is splitted into smaller texts
def text_split(extracted_data):
    # keeping size of each chunk to be 500 with overlap b/w chunks as 20
    text_splitter= RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap = 20)
    text_chunks= text_splitter.split_documents(extracted_data)

    return text_chunks




# Download the embeddig model
def download_hugging_face_embedding():
    embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding