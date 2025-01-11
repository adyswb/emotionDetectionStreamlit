import streamlit as st

def app():
    st.title("🌟 Welcome to bZar Psychiatrist!")
    st.markdown(
        """
        ### 🧠 About This App  
        This application leverages *deep learning* to detect emotions in facial expressions.  
        You can either upload an image or use your webcam to analyze emotions.

        ### ✨ Features:  
        - 📂 *Upload an image* to detect emotions.  
        - 🎥 Use a *real-time webcam feed* for emotion detection.

        Navigate to the *Emotion Detection* page to start!
        """
    )
    st.image("images/welcome_image.png", caption="Detect Emotions with AI", use_container_width=True)
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center;'>Empowering mental health with technology 🌈</p>",
        unsafe_allow_html=True
    )