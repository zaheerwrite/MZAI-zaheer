import streamlit as st
from groq import Groq

# Page Config
st.set_page_config(page_title="MZ AI Chat", layout="centered")
st.title("MZ Zaheer")

# Aap ki Groq API Key
client = Groq(api_key="Gsk_s1XvxzByj07gpj5PDCAEWGdyb3FYgGASMUqPIUmp42OTh6VxXxI9")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask MZ Zaheer anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        response = completion.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        st.error("Please check your API Key.")
