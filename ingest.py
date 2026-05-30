import os
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec



# Import varaibales

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")


# Load pdf documents

loader = PyPDFLoader(".\data\Medical_bookk.pdf")

documents = loader.load()

print(f"Total number of documents : {len(documents)}")


# filtering the documents


filtered_docs = []

for doc in documents:
    if doc.page_content and doc.page_content.strip():
        filtered_docs.append(doc)

# Add metadata
for doc in filtered_docs:
    doc.metadata["source_type"] = "pdf"
    doc.metadata["department"] = "general"


print(f"Loaded {len(filtered_docs)} valid documents")


#chunking 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)

docs = text_splitter.split_documents(filtered_docs)

print(f"Total number of documents after chunking : {len(docs)}")


# Initilizing embeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small", api_key=OPENAI_API_KEY
)

# Initilizing pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)


# Creating index

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name = INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

    print("Index has been created")

else:

    print("Index name is already exist")


vectoresotre = PineconeVectorStore.from_documents(
    documents=docs,
    index_name = INDEX_NAME,
    embedding=embeddings
    
)

print("Data store in pinecone vector store")