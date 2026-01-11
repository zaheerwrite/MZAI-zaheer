import streamlit as st
from groq import Groq

# Page Setup
st.set_page_config(page_title="MZ AI Chat", layout="centered")
st.title("MZ Zaheer")
st.markdown("<h3 style='text-align: right;'>محمد ظہیر مانسہرہ</h3>", unsafe_allow_html=True)

# Aap ki original API Key yahan bilkul sahi set kar di gayi hai
client = Groq(api_key="Gsk_s1XvxzByj07gpj5PDCAEWGdyb3FYgGASMUqPIUmp42OTh6VxXxI9")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat History Display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
if prompt := st.chat_input("Ask MZ Zaheer anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        # AI Response Generation
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        response = completion.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        # Error handling for API issues
        st.error(f"Error: {e}")
