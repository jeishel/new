import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Jeishel_Blog", page_icon=":heart:", layout="wide")

st.title("Content")
st.sidebar.success("Select a page above")
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/7662fdf8-e568-4b92-93ec-f95ddb206c78/4Bx21oXGex.json"

with st.container():
     st.title("Computer Programming: First-Year Perspective") 


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("The first Impression")
        st.write("##")
        st.write(
            """
            -As I stepped into the university halls, a blend of excitement and nerves surged through me. The world of computer engineering beckoned, promising both challenges and boundless opportunities. From day one, I was introduced to the foundational concepts—binary, algorithms, and the wonders of programming languages. It was like learning a secret language that unlocks the possibilities of technology.\n
            -Let's talk about those courses! Oh, the thrill and sometimes the slight terror of facing programming assignments. Debugging became my daily workout routine, and trust me, the satisfaction of fixing the bug after hours of contemplation is unmatched.\n
            -Ah, the eternal struggle of balancing academics, social life, and personal time. It's a fine-tuned juggling act. But I've learned that organization and time management are my trusty sidekicks in this endeavor.\n
            -The journey of a computer engineering freshman is a whirlwind—a mix of curiosity, challenges, and unending discoveries. Every line of code written is a step forward in understanding the complex yet captivating world of technology.\n
            -So, future freshmen or tech enthusiasts, join me in this exhilarating expedition as we unravel the mysteries of computer engineering, one line of code at a time!

            """ 
         )
        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("PROS AND CONS")
        st.write("##")
        st.write(
            """
            Computer programming offers numerous benefits and a few challenges as well. Here's a breakdown:\n
            **Pros:**\n
            1.Lucrative Career Opportunities: Programming skills are in high demand across industries, offering excellent job prospects and high salaries.\n
            2.Problem-Solving Skills: Programming teaches you to break down complex problems into smaller, manageable parts, enhancing your logical thinking and problem-solving abilities.\n
            3.Creativity: It's a creative field where you can build something from scratch, allowing for innovative solutions and unique creations.\n
            4.Flexibility: You can work remotely, freelance, or in an office, providing flexibility in work environments.\n
            5.Continuous Learning: Technology is constantly evolving, ensuring that there's always something new to learn, keeping the field dynamic and exciting.\n
            6.Global Community: Programming connects you with a vast global community of developers, fostering collaboration and shared knowledge.\n

            **Cons:**\n
            1.Steep Learning Curve: Initially, learning to code can be challenging and might require patience and perseverance to grasp programming concepts.\n
            2.Sedentary Work: Programming often involves long hours of sitting, which can impact physical health if not balanced with exercise and breaks.\n
            3.Frustration with Bugs: Debugging code can be frustrating and time-consuming, especially when dealing with complex errors.\n
            4.Rapid Technological Changes: Keeping up with the latest languages, frameworks, and tools can be overwhelming and require continuous learning.\n
            5.Isolation: Depending on work settings, programmers might spend long hours working alone, which can lead to a sense of isolation.\n
            6.Complexity: As projects grow larger, managing code complexity becomes more challenging, requiring good organizational skills.

            """ 
         )
        st.write("[Facebook account>](https://www.facebook.com/JEISHELRIVAS101/)")
    with right_column: 
        st_lottie(lottie_coding, height=300, key="coding")
    
