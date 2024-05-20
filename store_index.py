# pushing vector to vector DB (Pincone)

from src.helper import load_pdf, text_split, download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone
import pinecone
from pinecone import Pinecone, ServerlessSpec
import os
from langchain_pinecone import PineconeVectorStore

from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# print(PINECONE_API_KEY)

extracted_data = load_pdf("data/")      # load the data
text_chunks=text_split(extracted_data)  # create chunks
embeddings= download_hugging_face_embedding()   # download embedding model to create vectors


index_name = "medical-chatbot"

vectorstore_from_docs = PineconeVectorStore.from_documents(
        text_chunks,
        index_name=index_name,
        embedding=embeddings
)
