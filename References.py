import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Math App", layout="wide")

# Function to add background
# Function to add background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,{encoded}");
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# ✅ Use your correct image path here
add_bg_from_local("images/background/bg.png")


st.set_page_config(page_title="Student Portal", layout="wide")

