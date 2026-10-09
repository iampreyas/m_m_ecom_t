import streamlit as st 
from src.rag_engine import ProductRAGEngine
st.title("AI Trend Search")
engine = ProductRAGEngine()
q = st.text_input("Search:")
if st.button("Search") and q:
    results = engine.search(q)
    cols = st.columns(len(results))
    for i, item in enumerate(results):
        with cols[i]:
            if item.get('img'):
                st.image(item['img'],width=200)
            st.write(f"**{item['name']}** - Rs{item['price']}")
            st.write(f"*{item['desc']}*")