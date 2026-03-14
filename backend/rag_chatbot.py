import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Embeddings
embeddings = OpenAIEmbeddings()


# Vector store
vectorstore = PineconeVectorStore(
    index_name=os.getenv("INDEX_NAME"),
    embedding=embeddings
)


retriever = vectorstore.as_retriever()


# LLM
llm = ChatOpenAI(model="gpt-4o-mini")


# Prompt
prompt = ChatPromptTemplate.from_template(
    """Answer the question based only on the provided context.

    Context:
    {context}

    Question:
    {input}
    """
)


# Combine documents chain
document_chain = create_stuff_documents_chain(llm,prompt=prompt)

qa_chain = create_retrieval_chain(retriever, document_chain)


def ask_bot(question):
    result = qa_chain.invoke({"input": question})
    return result["answer"]

