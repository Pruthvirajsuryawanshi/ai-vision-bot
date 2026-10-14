from google import genai
from google.genai import types
import streamlit as st


#step 1: onoarding username and phone number

if 'onboarded' not in st.session.state:
    
st.title("microsnap ")
st.caption("eat it, count you nutrition, track your fitness... ")

with st.form("onboarding form"):
    name = st.text_input("Your Name")
    Whatsapp_number = st.text_input("Enter you whatsapp number", placeholder='+91 xxxxx xxxxx', help='this is the number so microsnap will call or text you.' )
     
