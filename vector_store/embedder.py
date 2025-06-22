# Embedding of JSON data (scraped from website)
import json
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI

load_dotenv()

# Load LLM model
llm_model = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

# Load Embedding model
embedding_model = AzureOpenAIEmbeddings(
    openai_api_key=os.getenv("AZURE_API_KEY"),
    azure_endpoint=os.getenv("EMBEDDING_AZURE_OPENAI_API_BASE"),
    azure_deployment=os.getenv("EMBEDDING_AZURE_OPENAI_API_NAME"),
    chunk_size=10
)

# Load cleaned JSON data
with open("../scrapper/books_clean.json") as f:
    books_data = json.load(f)

# Prepare documents for embedding
docs = []
for book in books_data:
    content = (
        f"Title: {book['title']}\n"
        f"Category: {book['category']}\n"
        f"Price: £{book['price']}\n"
        f"Availability: {book['availability']}\n"
        f"Rating: {book['rating']}/5"
    )
    docs.append(Document(page_content=content, metadata={"source": "books"}))

# Store embeddings in ChromaDB
vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="vectorstore/chroma_db"
)

# Save DB to disk
vector_db.persist()
print("✅ All book data embedded and stored in ChromaDB.")