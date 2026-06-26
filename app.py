import streamlit as st
import google.generativeai as genai

st.set_page_config(
   page_title="Gemini Chat with Memory",
   page_icon="💬",
   layout="centered"
)

st.title("Gemini Chat with Memory")
st.write("Ask a question, then ask a follow up. The app will remember the conversation during this session.")

try:
   api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
   st.error("Gemini API key is missing. Add GEMINI_API_KEY inside .streamlit/secrets.toml.")
   st.stop()

genai.configure(api_key=api_key)

model= genai.GenerativeModel("gemini-2.5-flash")


if "messages" not in st.session_state:
   st.session_state.messages = [
       {
           "role": "assistant",
           "content": "Hello. I am your Gemini assistant. Ask me something."
       }
   ]

def clear_chat():
   st.session_state.messages = [
       {
           "role": "assistant",
           "content": "Chat cleared. Ask me a new question."
       }
   ]

with st.sidebar:
   st.header("Chat Controls")
   st.button("Clear Chat", on_click=clear_chat)
   st.caption("This clears the conversation stored in Streamlit session state.")

for message in st.session_state.messages:
   with st.chat_message(message["role"]):
       st.write(message["content"])

user_input = st.chat_input("Ask something")

if user_input:
   st.session_state.messages.append(
       {
           "role": "user",
           "content": user_input
       }
   )

   with st.chat_message("user"):
       st.write(user_input)

   conversation_text = ""

   for message in st.session_state.messages:
       conversation_text += f"{message['role']}: {message['content']}\n"

   conversation_text += "assistant:"

   try:
       with st.spinner("Thinking..."):
        response = model.generate_content(
           contents=conversation_text
       )

       assistant_reply = response.text

   except Exception as error:
       assistant_reply = "Sorry, I could not generate a response. Please check your API key, model name, or internet connection."
       st.error(str(error))

   st.session_state.messages.append(
       {
           "role": "assistant",
           "content": assistant_reply
       }
   )

   with st.chat_message("assistant"):
       st.write(assistant_reply)
