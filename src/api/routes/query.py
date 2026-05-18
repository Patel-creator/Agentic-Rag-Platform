from fastapi import APIRouter
from pydantic import BaseModel

from src.retrieval.rag_service import rag_service


router = APIRouter()


class QueryRequest(BaseModel):

    question: str
    document_name: str | None = None


@router.post("/query")
async def query_rag(request: QueryRequest):

    result = rag_service.ask(
        request.question,
        request.document_name
    )

    return result