import streamlit as st
import cv2
from utils.face_recognition import verify_face
from utils.liveness_detection import check_liveness
from utils.blurriness_detection import is_blurry
from utils.behavior_monitoring import monitor_behavior
from utils.test_encryption import generate_key, encrypt_data, decrypt_data
import time

# Initialize state variables
last_detected_time = time.time()
key = generate_key()  # Encryption key

# Streamlit layout
st.title("Online Test Proctoring System")
st.write("Facial recognition, liveness detection, proctoring, and encryption in real-time.")

# File uploader for test taker's face
uploaded_file = st.file_uploader("Upload your image for recognition", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Blurriness check
    if is_blurry(image):
        st.error("The image is blurry, please upload a clearer image.")
    
    # Facial recognition
    # In a real case, you would compare the extracted embedding with a known face
    known_embedding = np.array([0.0])  # Placeholder for actual known face embedding
    if verify_face(image, known_embedding):
        st.success("Face verified successfully!")
    else:
        st.error("Face verification failed.")
    
    # Liveness detection
    if not check_liveness(image):
        st.error("Liveness check failed.")
    else:
        st.success("Liveness check passed.")
    
    # Behavior Monitoring
    face_detected = True  # Placeholder, should be based on real-time webcam feed
    monitoring_status = monitor_behavior(face_detected, last_detected_time)
    if monitoring_status != "Monitoring":
        st.warning(monitoring_status)

# Encryption Example for test response
test_response = st.text_input("Enter test response:")
if test_response:
    encrypted_response = encrypt_data(test_response, key)
    st.write(f"Encrypted Response: {encrypted_response}")
    decrypted_response = decrypt_data(encrypted_response, key)
    st.write(f"Decrypted Response: {decrypted_response}")