from langchain_community.vectorstores import Chroma


PERSIST_DIRECTORY = "chroma_db"


def get_vector_store(embeddings):

    vector_db = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    return vector_db


def add_documents(vector_db, chunks):

    vector_db.add_documents(chunks)

    return vector_db


def clear_vector_store(vector_db, source=None):

    if source:
        ids = vector_db.get(where={"source": source})["ids"]
    else:
        ids = vector_db.get()["ids"]
    
    if ids:
        vector_db.delete(ids=ids)