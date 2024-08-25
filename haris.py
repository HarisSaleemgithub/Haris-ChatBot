import google.generativeai as genai
import streamlit as st
GOOGLE_API_KEY = st.secrets["API-KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text
def get_chatbot_response(user_input):
    return getResponseFromModel(user_input)
st.set_page_config(page_title="Simple ChatBot",layout="centered")
st.title("🔎Haris ChatBot🔎")
st.write("POWERED BY GOOGLE GENERATIVE AI")
if "history" not in st.session_state:
    st.session_state["history"] = []
    # Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color: #e1ffc7;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")
    
    if submit_button:
         if user_input:
             response = get_chatbot_response(user_input)
             st.session_state.history.append((user_input, response))
             for user_message, bot_response in st.session_state.history:
                 st.write(f"**You:** {user_message}")
                 st.write(f"**Chatbot:** {bot_response}")
             else:
                 st.warning("Please Enter A Prompt")