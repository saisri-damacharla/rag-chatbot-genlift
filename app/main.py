#FastAPI app for RAG chatbot

from fastapi import FastAPI
from app.llm import get_llm_response
from app.retrieval import retrieve_documents

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    context = retrieve_documents(question)
    answer = get_llm_response(question, context)
    return {"answer": answer}
