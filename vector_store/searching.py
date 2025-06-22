# vector_store/searching.py

import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.chat_models import AzureChatOpenAI

load_dotenv()

# Load Embedding model (same config as used during saving)
embedding_model = AzureOpenAIEmbeddings(
    openai_api_key=os.getenv("AZURE_API_KEY"),
    azure_endpoint=os.getenv("EMBEDDING_AZURE_OPENAI_API_BASE"),
    azure_deployment=os.getenv("EMBEDDING_AZURE_OPENAI_API_NAME"),
    chunk_size=10
)

# Load vector DB
vector_db = Chroma(
    persist_directory="vectorstore/chroma_db",
    embedding_function=embedding_model
)

# Load LLM
llm_model = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7
)

def search_books(query, k=3):
    """Return top-k similar books from vector DB."""
    return vector_db.similarity_search(query, k=k)

def generate_llm_response(query, matched_docs):
    """Use Azure OpenAI to generate response from matched book docs."""
    context = "\n\n".join([doc.page_content for doc in matched_docs])
    prompt = f"""
You are a helpful book recommender bot. Based on the user's query below, and the book data provided, suggest the most suitable book(s) in a nice and helpful tone.

User query: "{query}"

Book Data:
{context}

Give your response in clear,short bullet points or paragraph format.

If user asks about out of context like something else like about weather or anything else then say Sorry, I'm not able to help you in that manner. Ask me about something else in friendly tone.
"""

    return llm_model.predict(prompt)
