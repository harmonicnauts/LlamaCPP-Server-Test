from openai import OpenAI 
import streamlit as st 

# Initialize OpenAI client with base URL and API key
client = OpenAI(
    base_url="http://localhost:8000/v1",  # Base URL for OpenAI API
    api_key="123",
)

# If "messages" not in session state, initialize it with a default system message
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            # Role of the message
            "role": "system", 
            "content": """You are an AI Assistant to help user code their projects. If you do not know the answer, reply I don't know 
                don't make things up.""",  # Content of the message
        }
    ]

st.title("🤖 LLaMa.CPP Python (Mistral 7B Test)")

print(st.session_state)

# Iterate through stored messages and display them as chat messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

# Input prompt for user
prompt = st.chat_input("Pass your input here")

if prompt:
    # Display user input as a chat message
    st.chat_message("user").markdown(prompt)
    
    # Append user input to session state messages
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using OpenAI's chat API
    response = client.chat.completions.create(
        model="llama.cpp/models/mistral-7b-instruct-v0.1.Q2_K.gguf", 
        messages=st.session_state.messages,
        stream=True,
    )

    complete_response = "" 

    # Display assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                complete_response += chunk.choices[0].delta.content
                message_placeholder.markdown(complete_response + "▌")
                message_placeholder.markdown(complete_response)
    
    # Append assistant's response to session state messages
    st.session_state.messages.append(
        {"role": "assistant", "content": complete_response}
    )
