import streamlit as st
from groq import Groq

# App design
st.set_page_config(page_title="My AI App", layout="centered")
st.title("🤖 میرا اپنا اے آئی")

# Apni Groq API Key yahan likhen
GROQ_API_KEY = "آپ_کی_گروک_کی_یہاں_آئے_گی"

client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("مجھ سے کچھ پوچھیں..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
