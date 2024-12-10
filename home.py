import streamlit as st

def app():
    st.title("Welcome to bZar Psychiatrist!")
    st.markdown("""
    ### About This App
    This application uses deep learning to detect emotions in facial expressions.  
    You can either upload an image or use your webcam to analyze emotions.

    ### Features:
    - Upload an image to detect emotions.
    - Use a real-time webcam feed for emotion detection.

    Navigate to the **Emotion Detection** page to start!
    """)

    # Add any additional content or design
    st.image("images/welcome_image.jpg", caption="Detect Emotions with AI", use_container_width=True)
