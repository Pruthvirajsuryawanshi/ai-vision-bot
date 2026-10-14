from google import genai
from google.genai import types
import streamlit as st
from prompts import SYSTEM_PROMPT

MODEL_NAME = "gemini-3.8-flash"


@st.cache_resource
def gemini_client():
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


st.title("microsnap")
st.caption("eat it, count your nutrition, track your fitness...")

if not st.session_state.get("onboarded", False):
    with st.form("onboarding form"):
        name = st.text_input("Your Name")
        whatsapp_number = st.text_input(
            "Enter your WhatsApp number",
            placeholder="+91 xxxxx xxxxx",
            help="This is the number Microsnap will use to call or text you.",
        )
        submitted = st.form_submit_button("Let's go")

    if submitted:
        name = name.strip()
        whatsapp_number = whatsapp_number.strip()
        if not name or not whatsapp_number:
            st.warning("Please fill in your name and WhatsApp number.")
        else:
            st.session_state.name = name
            st.session_state.whatsapp_number = whatsapp_number
            st.session_state.chat = gemini_client().chats.create(
                model=MODEL_NAME,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT
                ),
            )
            st.session_state.messages = []
            st.session_state.onboarded = True
            st.rerun()
else:
    st.success(f"Welcome, {st.session_state.name}!")
