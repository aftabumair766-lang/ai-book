from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Offline RAG Chatbot")

# Simple in-memory "vector database"
docs = {}
for i in range(1, 11):
    with open(f"docs/chapter_{i}.md", "r", encoding="utf-8") as f:
        docs[f"chapter_{i}"] = f.read()

class Query(BaseModel):
    question: str
    context: str = None  # Optional: specific chapter

@app.post("/ask")
def ask_question(query: Query):
    if query.context and query.context in docs:
        answer = f"[Answer from {query.context}]: {docs[query.context][:150]}..."
    else:
        # Return first 150 chars from all chapters as mock
        combined = "\n".join(docs.values())
        answer = f"[Answer from book]: {combined[:150]}..."
    return {"answer": answer}
