import streamlit as st
from groq import Groq

# Page Layout
st.set_page_config(page_title="MZ AI Chat", layout="centered")
st.title("MZ Zaheer")
st.markdown("<h3 style='text-align: right;'>محمد ظہیر مانسہرہ</h3>", unsafe_allow_html=True)

# Aap ki Bilkul Sahih aur Original API Key
client = Groq(api_key="Gsk_nIW1tJ8GoVNeBfvvPUkqWGdyb3FYagxIcFpMsJlwnlDkJQ1ciChK")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
if prompt := st.chat_input("Ask MZ Zaheer anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        # AI Response
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        response = completion.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        # Error details
        st.error(f"Error: {e}")
