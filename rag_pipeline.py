import json
import faiss
import numpy as np
import requests
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base
with open("knowledge_base.json", "r") as f:
    data = json.load(f)

documents = [
    item["title"] + ". " + item["problem"] + " " + item["solution"]
    for item in data
]

# Create embeddings
embeddings = embedding_model.encode(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


# -----------------------------
# Retrieval
# -----------------------------
def retrieve(query, k=3):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    results = [documents[i] for i in indices[0]]
    return results


# -----------------------------
# Answer Query Using ScaleDown
# -----------------------------
def answer_query(query):

    # Step 1: Retrieve relevant docs
    retrieved_docs = retrieve(query)
    combined_context = "\n\n".join(retrieved_docs)

    # Step 2: Call ScaleDown REST API
    url = "https://api.scaledown.xyz/compress/raw/"

    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "context": combined_context,
        "prompt": query,
        "model": "gpt-4o",
        "scaledown": {"rate": "auto"}
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"ScaleDown Error: {response.text}"

    data = response.json()

    if data["successful"]:
        compressed_text = data["results"]["compressed_prompt"]
        compression_ratio = data["results"]["compression_ratio"]
        tokens_before = data["results"]["original_prompt_tokens"]
        tokens_after = data["results"]["compressed_prompt_tokens"]

        formatted_output = f"""

### 🔍 Solution

{compressed_text}

---

### 📊 Token Optimization

- Original Tokens: {tokens_before}
- Compressed Tokens: {tokens_after}
- Compression Ratio: {round(compression_ratio * 100, 2)}%
        """

        return formatted_output

    else:
        return "Compression failed."


