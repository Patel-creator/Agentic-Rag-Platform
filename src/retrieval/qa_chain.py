from langchain_classic.chains import RetrievalQA
from langchain_ollama import ChatOllama


def build_qa_chain(vector_db):

    llm = ChatOllama(
        model="phi3:mini"
    )

    retriever = vector_db.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain