import streamlit as st

def app():
    st.title("Contact Us")
    st.write("We'd love to hear from you! You can reach out to us. Send us an email :)")

    # Email configuration
    email_address = "badriyahsaid12@gmail.com"  # Replace with your email
    subject = "Inquiry from Emotion Detection App"  # Customize the subject
    body = "Hello,%0A%0AI would like to inquire about..."  # Prefilled message

    # JavaScript to open mail client on button click
    mailto_link = f"mailto:{email_address}?subject={subject}&body={body}"
    st.markdown(
        f"""
        <a href="{mailto_link}" target="_blank">
            <button style="background-color:#4CAF50; color:white; padding:10px 24px; border:none; cursor:pointer; border-radius:5px;">
                📧 Email Us
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
