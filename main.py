from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "FastAPI + Groq running 🚀"}

@app.post("/query")
def query_rag(data: Query):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": data.question}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }
