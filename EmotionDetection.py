import streamlit as st
import cv2
from keras.models import model_from_json
import numpy as np
import os
import datetime
from collections import Counter

# Function to provide a suggestion based on emotion
def get_suggestion(emotion):
    suggestions = {
        "angry": {
            "message": "Take a deep breath and count to 10. Try journaling your thoughts to release frustration.",
            "link": "https://www.google.com/search?q=what+can+you+do+if+you+are+angry"
        },
        "fear": {
            "message": "Talk to someone you trust about your concerns. Practice deep breathing.",
            "link": "https://www.google.com/search?q=what+can+you+do+if+you+are+fear"
        },
        "happy": {
            "message": "Share your happiness with someone close to you. Capture the moment in a journal.",
            "link": "https://www.google.com/search?q=what+can+you+do+if+you+are+happy"
        },
        "neutral": {
            "message": "Take a short walk to refresh yourself. Listen to uplifting music.",
            "link": "https://www.google.com/search?q=what+can+you+do+if+you+are+feel+neutral"
        },
        "sad": {
            "message": "Reach out to a friend or family member. Engage in an activity you enjoy, like drawing or exercising.",
            "link": "https://www.google.com/search?q=what+can+you+do+if+you+are+feel+sad"
        },
        "surprise": {
            "message": "Share your experience with someone. Take a moment to reflect on the situation.",
            "link": "https://www.google.com/search?q=what+can+you+do+if+you+are+feel+surprise"
        },
    }
    return suggestions.get(emotion, {"message": "No suggestion available.", "link": None})

def app():
    st.title("Emotion Detection")
    mode = st.radio("Choose Mode", ("Upload Image", "Use Webcam"))
    dominant_emotions = Counter()

    # Load pre-trained model
    try:
        with open("emotiondetector.json", "r") as json_file:
            model_json = json_file.read()
        model = model_from_json(model_json)
        model.load_weights("emotiondetector.h5")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

    # Load Haar cascade for face detection
    haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(haar_file)

    # Define a function to extract features from an image
    def extract_features(image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = gray_image.reshape(1, 48, 48, 1)  # Use 1 channel for grayscale image
        return feature / 255.0

    # Define labels for emotion classes
    labels = {0: 'angry', 1: 'fear', 2: 'happy', 3: 'neutral', 4: 'sad', 5: 'surprise', 6: 'unknown emotion'}

    if mode == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file:
            try:
                # Read and decode the uploaded file
                image_data = np.frombuffer(uploaded_file.read(), np.uint8)
                image = cv2.imdecode(image_data, 1)
                
                if image is None:
                    st.error("Invalid image format. Please upload a valid file.")
                    return
                
                # Detect faces and process
                faces = face_cascade.detectMultiScale(image, 1.3, 5)
                if len(faces) == 0:
                    st.warning("No faces detected in the uploaded image.")
                else:
                    for (x, y, w, h) in faces:
                        face_image = cv2.resize(image[y:y + h, x:x + w], (48, 48))
                        img = extract_features(face_image)
                        pred = model.predict(img)
                        predicted_emotion = labels[pred.argmax()]
                        dominant_emotions[predicted_emotion] += 1
                        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(image, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB", caption="Emotion Detection Result")

                    # Get the most dominant emotion and provide suggestion
                    if dominant_emotions:
                        most_common_emotion = dominant_emotions.most_common(1)[0][0]
                        suggestion = get_suggestion(most_common_emotion)
                        st.subheader(f"Detected Emotion: {most_common_emotion.capitalize()}")
                        st.write(f"Suggestion: {suggestion['message']}")
                        
                        # Display clickable button for the Google search link
                        if suggestion["link"]:
                            st.markdown(
                                f"""
                                <a href="{suggestion['link']}" target="_blank">
                                    <button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; cursor:pointer; border-radius:5px;">
                                        Click Here for More Suggestions
                                    </button>
                                </a>
                                """,
                                unsafe_allow_html=True,
                            )
            except Exception as e:
                st.error(f"An error occurred while processing the image: {e}")

    elif mode == "Use Webcam":
        save_video = st.checkbox("Save Video")
        run_webcam = st.checkbox("Start Webcam")

        if run_webcam:
            cap = cv2.VideoCapture(0)
            if save_video:
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                video_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".avi"
                video_path = os.path.join("videos", video_name)
                os.makedirs("videos", exist_ok=True)
                out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))

            prev_emotion = None
            frame_placeholder = st.empty()
            emotion_placeholder = st.empty()
            suggestion_placeholder = st.empty()

            try:
                while run_webcam:
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Failed to access webcam.")
                        break

                    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_image = cv2.resize(frame[y:y + h, x:x + w], (48, 48))
                        img = extract_features(face_image)
                        pred = model.predict(img)
                        predicted_emotion = labels[pred.argmax()]
                        dominant_emotions[predicted_emotion] += 1
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(frame, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

                    if dominant_emotions:
                        most_common_emotion = dominant_emotions.most_common(1)[0][0]
                        if most_common_emotion != prev_emotion:
                            prev_emotion = most_common_emotion
                            current_suggestion = get_suggestion(most_common_emotion)
                            emotion_placeholder.markdown(f"**Emotion Detected: {most_common_emotion.capitalize()}**")
                            suggestion_placeholder.markdown(f"**Suggestion: {current_suggestion['message']}**")

                    if save_video:
                        out.write(frame)

            finally:
                cap.release()
                if save_video:
                    out.release()
