# 🔧 Technical Troubleshooting Guide (RAG + ScaleDown)

An enterprise-style AI-powered troubleshooting assistant built using
Retrieval-Augmented Generation (RAG) and ScaleDown context compression.

This system retrieves relevant IT issues from a knowledge base,
compresses context intelligently, and generates optimized technical
solutions while reducing token usage.

------------------------------------------------------------------------

## 🚀 Project Overview

Traditional chatbots send entire documents to LLMs, increasing token
cost and reducing efficiency.

This project demonstrates:

-   Semantic retrieval using FAISS
-   Context compression using ScaleDown API
-   GPT-4o integration via ScaleDown
-   Token optimization metrics
-   Enterprise-style structured responses

------------------------------------------------------------------------

## 🧠 Architecture

User Query\
↓\
Sentence Transformer Embedding\
↓\
FAISS Vector Search (Top-K Retrieval)\
↓\
Context Compression (ScaleDown)\
↓\
GPT-4o via ScaleDown\
↓\
Structured Technical Response

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python\
-   Streamlit (UI)\
-   FAISS (Vector Search)\
-   Sentence Transformers (Embeddings)\
-   ScaleDown API (Context Compression + LLM)\
-   GPT-4o (via ScaleDown)

------------------------------------------------------------------------

## 📂 Project Structure

technical-troubleshooting-rag/

├── app.py\
├── rag_pipeline.py\
├── knowledge_base.json\
├── requirements.txt\
├── .env\
└── README.md

------------------------------------------------------------------------

## 🔍 How It Works

### 1️⃣ Retrieval (RAG)

-   User query is converted into embeddings\
-   FAISS retrieves top relevant troubleshooting entries\
-   Only relevant context is selected

### 2️⃣ Context Compression

-   ScaleDown compresses retrieved context\
-   Removes irrelevant tokens\
-   Optimizes prompt before model call

### 3️⃣ Generation

-   GPT-4o generates structured troubleshooting output\
-   Response includes:
    -   Issue detected\
    -   Root cause\
    -   Resolution steps\
    -   Optimization metrics

------------------------------------------------------------------------

## 📊 Token Optimization

The system displays:

-   Original token count\
-   Compressed token count\
-   Compression efficiency percentage

Example:\
- Original Tokens: 115\
- Compressed Tokens: 32\
- \~72% token reduction

This demonstrates real-world GenAI cost optimization.

------------------------------------------------------------------------

## 💻 Installation & Setup

### 1️⃣ Clone Repository

git clone `<your-repo-link>`\
cd technical-troubleshooting-rag

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Add Environment Variables

Create a `.env` file:

SCALEDOWN_API_KEY=your_api_key_here

### 4️⃣ Run Application

streamlit run app.py

------------------------------------------------------------------------

## 🧪 Example Queries

-   WiFi not working\
-   Laptop overheating\
-   Excel not opening\
-   VPN not connecting\
-   High CPU usage\
-   USB device not recognized

------------------------------------------------------------------------

## ✨ Key Features

✔ Retrieval-Augmented Generation (RAG)\
✔ Semantic similarity search\
✔ Context compression using ScaleDown\
✔ Token usage tracking\
✔ Enterprise-style structured output\
✔ Real-world IT troubleshooting dataset

------------------------------------------------------------------------

## 📈 Why This Project Matters

In production AI systems:

-   Token cost directly impacts API billing\
-   Sending large prompts increases latency\
-   Context compression improves efficiency

This project simulates an enterprise AI pipeline optimized for cost,
speed, and accuracy.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add similarity score visualization\
-   Add document upload support\
-   Add logging and analytics dashboard\
-   Deploy on Streamlit Cloud\
-   Expand to server-level and cloud-level troubleshooting

------------------------------------------------------------------------

## 👨‍💻 Author

Built as part of GenAI Internship Program (Session 2 -- RAG Systems).
