from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = i

    return chunks