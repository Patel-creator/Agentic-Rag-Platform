from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:mini")

response = llm.invoke("Explain RAG simply")

print(response.content)
