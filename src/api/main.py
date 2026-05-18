from fastapi import FastAPI

from src.api.routes.ingest import router as ingest_router
from src.api.routes.query import router as query_router


app = FastAPI(
    title="Agentic RAG Platform"
)


@app.get("/")
def home():

    return {
        "message": "RAG API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


app.include_router(ingest_router)
app.include_router(query_router)