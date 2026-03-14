import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")

loader = TextLoader(r"data\stock_info.txt")
docs = loader.load()


splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = splitter.split_documents(docs)



embeddings = OpenAIEmbeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)


if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

    print("Index name has been created")

else:
    print("Index_name is already exist")

    
vector_store = PineconeVectorStore.from_documents(
    documents=documents,
    embedding=embeddings,
    index_name = INDEX_NAME
)


print("Data uploaded to Pinecone")