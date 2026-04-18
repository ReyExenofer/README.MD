from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="GROQ_API_KEY",
    model_name="gemma2-9b-it",
    temperature=0
)
