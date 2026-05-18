# Agentic RAG Platform

A platform to process documents (like PDFs) and perform Retrieval-Augmented Generation (RAG) using local or hosted LLMs.

## Setup on a New Device

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Patel-creator/Agentic-Rag-Platform.git
   cd Agentic-Rag-Platform
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory if necessary (e.g., for API keys or Ollama host URLs).

## Usage

1. **Add Documents**
   Place any PDF documents you want to process in the `data/` folder.

2. **Run Tests / API**
   To test the RAG flow via the terminal, you can modify and run `rag_test.py`:
   ```bash
   python rag_test.py
   ```

   To start the API or frontend, run the respective starting scripts (e.g., `uvicorn src.api.main:app --reload` or `streamlit run frontend/app.py` depending on your setup).
