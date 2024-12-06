import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load pre-trained FaceNet model
model = load_model('facenet_keras.h5')

def extract_face(image):
    # Convert image to RGB and preprocess
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (160, 160))  # FaceNet input size
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize

    # Perform face recognition
    embeddings = model.predict(img)
    return embeddings

def verify_face(image, known_embedding):
    embeddings = extract_face(image)
    dist = np.linalg.norm(embeddings - known_embedding)
    if dist < 0.6:  # You can adjust this threshold
        return True
    return False
