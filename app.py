import streamlit as st 
from src.rag_engine import ProductRAGEngine
st.title("AI Trend Search")
engine = ProductRAGEngine()
st.sidebar.header("Filters")
category=st.sidebar.selectbox("Select Category",["All","Hoodies","Bottoms","Tees"])
q = st.text_input("Search:")
results=engine.search(q,category)
if results:
    cols = st.columns(len(results))
    for i, item in enumerate(results):
        with cols[i]:
            if item.get('img'):
                st.image(item['img'],width=200)
            st.write(f"**{item['name']}** - Rs{item['price']}")
            st.write(f"*Trend Score: {item.get('trend_score',85)}%*")
            st.write(f"*{item['desc']}*")
else:
    st.warning("No matching trends found!")