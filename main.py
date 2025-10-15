# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

# Load environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL", "https://api.gemini.com/v1/chat")

app = FastAPI(title="Gemini Chatbot API")

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=QueryResponse)
def chat_backend(request: QueryRequest):
    user_q = request.question.strip()

    # Call Gemini API
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    payload = {"prompt": user_q}

    try:
        resp = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        resp.raise_for_status()
        answer = resp.json().get("answer", "No answer returned by Gemini.")
    except Exception as e:
        answer = f"⚠️ Error: {e}"

    return QueryResponse(answer=answer)
