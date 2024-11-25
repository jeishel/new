
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Jeishel_Blog", page_icon=":heart:", layout="wide")

st.title("Main Page")
st.sidebar.success("Select a page above")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/7662fdf8-e568-4b92-93ec-f95ddb206c78/4Bx21oXGex.json"


with st.container():
    st.subheader("Hi, I'm Jeishel Rivas :wave:")
    st.title("Find out how interesting Computer Engineering is through my blog")
    st.write("Hey there, fellow tech enthusiast! Ready to dive into the wild world of Computer Engineering with me? Buckle up because I'm about to spill the beans on the highs and lows of being a Computer Engineer in the making. Welcome to my corner of the internet, where we're about to unravel the rollercoaster ride of Pros and Cons that come with the badge of being a Computer Engineering student. Let's get this byte-sized adventure started! 💻✨")
    st.write("[Message me in gmail >] jrivas2@ssct.edu.ph")


with st.container():
     st.title("Computer Programming: First-Year Perspective") 


with st.container():     
     image_file_path = "Untitled_design-removebg-preview.PNG"
     st.image(image_file_path, caption="Rivas, Jeishel C.")


    


