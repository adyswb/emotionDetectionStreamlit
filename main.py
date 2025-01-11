import streamlit as st
from home import app as home_app
from EmotionDetection import app as emotion_detection_app
from contact_us import app as contact_us_app

# Set page configuration
st.set_page_config(
    page_title="bZar Psychiatrist",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for black icon and divider line
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #fffaf0; /* Soft cream background */
    }

    /* Sidebar container */
    section[data-testid="stSidebar"] {
        background-color: #fefcf5; /* Light cream for the sidebar */
        border: 1px solid #e6e6e6; /* Subtle border for definition */
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); /* Shadow for depth */
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] .css-1lcbmhc, section[data-testid="stSidebar"] .css-18e3th9 {
        color: #4a4a4a; /* Dark gray for sidebar text */
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] .css-1lcbmhc {
        font-size: 1.2em;
        font-weight: bold;
    }

    /* Style for the collapse icon "<" */
    section[data-testid="stSidebar"] .css-1v3fvcr {
        color: black; /* Ensure the icon is fully visible with black */
        font-size: 1.5em; /* Adjust size if necessary */
    }

    /* Divider line under Navigation */
    section[data-testid="stSidebar"] hr {
        border-color: black; /* Set the divider line to black */
    }

    /* General text styling for headings */
    h1, h2, h3, h4, h5, h6, p, li {
        color: #3e3e3e; /* Neutral gray text */
    }

    /* Font for overall consistency */
    body {
        font-family: 'Verdana', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for navigation
st.sidebar.title("🔍 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Go to", 
    ["🏠 Home", "📊 Emotion Detection", "📧 Contact Us"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("💡 <small>Scan Yours with bZar!</small>", unsafe_allow_html=True)

# Page routing
if page == "🏠 Home":
    home_app()
elif page == "📊 Emotion Detection":
    emotion_detection_app()
elif page == "📧 Contact Us":
    contact_us_app()