import requests
import streamlit as st


API_BASE = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Agentic RAG Platform",
    layout="wide"
)

st.title("Agentic RAG Platform")

st.markdown(
    "Upload PDFs and chat with your documents."
)

# -------------------------
# Upload Section
# -------------------------

st.header("Upload PDF")

uploaded_file = st.file_uploader(
    "Choose PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    if st.button("Ingest PDF"):

        with st.spinner("Ingesting document..."):

            response = requests.post(
                f"{API_BASE}/ingest",
                files=files
            )

        if response.status_code == 200:

            st.success("PDF ingested successfully")

            st.json(response.json())

        else:

            st.error("Ingestion failed")


# -------------------------
# Chat Section
# -------------------------

st.header("Ask Questions")

query = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    with st.spinner("Generating answer..."):

        response = requests.post(
            f"{API_BASE}/query",
            json={
                "question": query,
                "document_name": uploaded_file.name
            }
        )

    if response.status_code == 200:

        result = response.json()

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Sources")

        for source in result["sources"]:

            st.write(
                f"📄 {source['source']} | Page {source['page']}"
            )

    else:

        st.error("Query failed")