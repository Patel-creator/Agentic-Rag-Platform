from src.ingestion.loader import load_pdf
from src.ingestion.chunker import split_documents

from src.retrieval.embeddings import get_embedding_model
from src.retrieval.vector_store import (
    get_vector_store,
    add_documents,
    clear_vector_store
)

from langchain_ollama import ChatOllama


class RAGService:

    def __init__(self):

        self.embeddings = get_embedding_model()

        self.vector_db = get_vector_store(
            self.embeddings
        )

        self.llm = ChatOllama(
            model="phi3:mini"
        )

    def ingest_pdf(self, pdf_path):

        documents = load_pdf(pdf_path)

        chunks = split_documents(documents)

        clear_vector_store(self.vector_db, source=pdf_path)

        if chunks:
            add_documents(
                self.vector_db,
                chunks
            )

        return len(chunks)

    def ask(self, query, document_name=None):

        retriever = self.vector_db.as_retriever(
            search_kwargs={
                "k": 3
            }
        )

        if document_name:

            docs = self.vector_db.similarity_search(
                query,
                k=3,
                filter={
                    "document_name": document_name
                }
            )

        else:

            docs = retriever.get_relevant_documents(query)

        # BUILD CONTEXT
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say "I could not find the answer in the document."

Context:
{context}

Question:
{query}
"""

    response = self.llm.invoke(prompt)

    sources = []

    for doc in docs:

        source = {
            "source": doc.metadata.get("source"),
            "page": doc.metadata.get("page")
        }

        if source not in sources:
            sources.append(source)

    return {
        "answer": response.content,
        "sources": sources
    }


rag_service = RAGService()