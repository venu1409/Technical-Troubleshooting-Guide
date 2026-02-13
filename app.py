import streamlit as st
from rag_pipeline import answer_query

st.title("🔧 Technical Troubleshooting Guide (RAG)")

query = st.text_input("Describe your issue:")

if st.button("Get Solution"):
    if query:
        response = answer_query(query)
        st.markdown(response)
