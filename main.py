import streamlit as st
from home import app as home_app
from EmotionDetection import app as emotion_detection_app
from contact_us import app as contact_us_app

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Emotion Detection", "Contact Us"])

if page == "Home":
    home_app()
elif page == "Emotion Detection":
    emotion_detection_app()
elif page == "Contact Us":
    contact_us_app()
