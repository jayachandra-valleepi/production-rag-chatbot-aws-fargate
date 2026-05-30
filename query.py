import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Import varaibales

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")


# Initilizing embeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small", api_key=OPENAI_API_KEY
)

#vectore store

vectorestore = PineconeVectorStore.from_existing_index(
    index_name=INDEX_NAME,
    embedding=embeddings
)



#retriever 

retriever = vectorestore.as_retriever(search_type = "similarity", search_kwargs = {"k" : 3})


#llm

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)


# MEMORY

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# prompt

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a friendly medical AI assistant.

Rules:
1. If the user greets you (hi, hello, hey, good morning), greet naturally.
2. If the user does casual conversation, reply normally.
3. If the user asks a medical question, answer ONLY from the provided context.
4. If medical information is not available in the context, say:
"I don't have enough medical information."

Context:
{context}

Question:
{question}

Answer:
"""
)


# rag chain

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    chain_type="stuff",
    combine_docs_chain_kwargs={
        "prompt": prompt
    }
)

def get_response(question):

    result = qa_chain.invoke({
        "question": question
    })

    return result["answer"]

# if __name__=="__main__":
#      while True:
#         q = input("\nPlease ask your query: ")
#         print(get_response(q))

    
