from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains.retrieval_qa.base import RetrievalQA
from config import OPENAI_API_KEY, PINECONE_API_KEY, INDEX_NAME

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)


vector_store = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings
)


retriever = vector_store.as_retriever()

llm = ChatOpenAI(model = "gpt-4o-mini")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)


def ask_bot(question):
    response = qa_chain.run(question)
    return response