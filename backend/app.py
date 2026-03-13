from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag_pipeline import ask_bot
from backend.stock_data import get_stock_price


app = FastAPI()

class Question(BaseModel):
    query:str

@app.post("/chat")

def chat(q:Question):
    if "price" in q.query:
        stock = q.query.split()[-1]
        return {"response" : get_stock_price(stock)}
    

    answer = ask_bot(q.query)

    return {"response" : answer}
