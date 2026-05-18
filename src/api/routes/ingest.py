from fastapi import APIRouter, UploadFile, File
import shutil

from src.retrieval.rag_service import rag_service


router = APIRouter()


@router.post("/ingest")
async def ingest_pdf(file: UploadFile = File(...)):

    save_path = f"data/{file.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunk_count = rag_service.ingest_pdf(
        save_path
    )

    return {
        "message": f"{file.filename} ingested",
        "chunks": chunk_count
    }