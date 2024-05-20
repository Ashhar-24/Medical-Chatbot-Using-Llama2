import os
from flask import Flask, render_template, request
from langchain_pinecone import PineconeVectorStore
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from src.prompt import *
from src.helper import download_hugging_face_embedding
# from store_index import vectorstore_from_docs


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# download embedding model to create vectors
embeddings = download_hugging_face_embedding()

index_name = "medical-chatbot"

vectorstore_from_docs = PineconeVectorStore.from_existing_index(
    index_name, embeddings)


PROMPT = PromptTemplate(template=prompt_template,
                        input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}


try:
    llm = CTransformers(
        model='model/llama-2-7b-chat.ggmlv3.q2_K.bin',
        model_type="llama",
    )
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load the model: {e}")


qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_from_docs.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])


if __name__ == '__main__':
    app.run(debug=True)
