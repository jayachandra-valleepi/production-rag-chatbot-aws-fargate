from fastapi import FastAPI
from backend.rag_chatbot import ask_bot
from backend.stock_tool import get_stock_price

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Stock Chatbot Running"}


@app.get("/chat")
def chat(q:str):

    if "price" in q.lower():

        symbol = q.split()[-1].upper()

        return {"response": get_stock_price(symbol)}
    
    response = ask_bot(q)

    return {"response":response}