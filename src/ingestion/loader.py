from langchain_community.document_loaders import PyPDFLoader
import os


def load_pdf(pdf_path: str):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    filename = os.path.basename(pdf_path)

    for doc in documents:

        doc.metadata["source"] = pdf_path
        doc.metadata["document_name"] = filename

    return documents