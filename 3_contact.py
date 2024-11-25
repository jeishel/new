import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Jeishel_Blog", page_icon=":heart:", layout="wide")

st.title("Contact")
st.sidebar.success("Select a page above")

st.header(":mailbox: Get in Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/rivasjeishel@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style.css>", unsafe_allow_html=True)

local_css("style/style.css")
    
