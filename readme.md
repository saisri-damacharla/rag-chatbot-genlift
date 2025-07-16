# RAG Chatbot

A Retrieval-Augmented Generation chatbot that uses FAISS or Pinecone to find relevant context from documents, and LLMs (OpenAI or Hugging Face) to answer queries.

## Features
- FastAPI backend
- Retrieval system using FAISS/Pinecone
- LLM response generation (OpenAI or local models)
- Dockerized for deployment

## Run
```
docker build -t rag-chatbot .
docker run -p 8000:8000 rag-chatbot
```

Access at `http://localhost:8000/ask?question=What+is+RAG?`
