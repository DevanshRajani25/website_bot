# 📚 मेरी Book - AI Book Recommender Chatbot 🤖✨ <br/>

![Screenshot 2025-06-22 160852](https://github.com/user-attachments/assets/f81f8af3-1c5d-4615-8588-b238e30078fe)

![Screenshot 2025-06-22 160920](https://github.com/user-attachments/assets/713d60c8-1caa-49e5-bd38-9c4fcfe161f7)

![Screenshot 2025-06-22 160955](https://github.com/user-attachments/assets/834bf032-0acb-4f63-9078-37779a90bfd8)



🚀 A Personalized Book Recommendation Bot that combines 💻 web scraping, 🧠 LLMs, 🗃️ Vector Search, and an intuitive 🎨 Streamlit UI! <br/>


## 🧠 What is "मेरी Book"? <br/>

**"मेरी Book"** is an intelligent AI chatbot that understands your reading preferences in natural language and recommends the perfect book for you — using real scraped data and powerful LLM reasoning! <br/>
It combines **data scraping**, **RAG (Retrieval-Augmented Generation)**, and **LLMs** to create a smart, contextual, and friendly assistant.<br/>

## 🔁 End-to-End Workflow 💪<br/>

```mermaid
graph LR
A[🔍 Scrape Book Data from Website] --> B[🧹 Clean + Format as JSON]
B --> C[📄 Convert JSON to Documents]
C --> D[🔗 Embed with AzureOpenAI Embeddings]
D --> E[📦 Store in Chroma Vector DB]
E --> F[🎙️ Streamlit Chat UI for Input]
F --> G[🧠 Query VectorDB → Get Similar Books]
G --> H[🧾 Format Response with Azure GPT-4o]
H --> I[💬 Final Output in Streamlit]
