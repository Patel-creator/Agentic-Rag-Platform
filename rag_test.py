from src.ingestion.loader import load_pdf
from src.ingestion.chunker import split_documents

from src.retrieval.embeddings import get_embedding_model
from src.retrieval.vector_store import create_vector_store
from src.retrieval.qa_chain import build_qa_chain


PDF_PATH = "data/sample.pdf"


# Load PDF
documents = load_pdf(PDF_PATH)

print(f"Loaded {len(documents)} pages")


# Split
chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks")


# Embeddings
embeddings = get_embedding_model()


# Vector DB
vector_db = create_vector_store(chunks, embeddings)

print("Vector DB created")


# QA Chain
qa_chain = build_qa_chain(vector_db)

print("RAG system ready")


while True:

    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    response = qa_chain.invoke(query)

    print("\nAnswer:")
    print(response["result"])