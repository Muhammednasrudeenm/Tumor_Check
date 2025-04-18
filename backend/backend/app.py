from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
import tensorflow as tf
import os
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

# ✅ Google Drive File ID of the .h5 model
FILE_ID = "1DdZcp5DruoPU2T9ZdH34c37dYBvn9K9k"  # Replace with your actual File ID
MODEL_PATH = "final_model.h5"  # Local path for model storage

# ✅ Download model from Google Drive if not exists
if not os.path.exists(MODEL_PATH):
    print("📥 Downloading model from Google Drive...")
    url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
    response = requests.get(url)
    with open(MODEL_PATH, "wb") as file:
        file.write(response.content)
    print("✅ Model downloaded successfully.")

# ✅ Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# ✅ Class labels
CLASS_LABELS = ["Glioma", "Meningioma", "Notumor", "Pituitary","Please Upload Brain MRI image "]

def preprocess_image(image_bytes):
    """Resize and preprocess image for prediction."""
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize((299, 299))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0) 
    return image

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload and return tumor classification."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        print(f"✅ Received file: {file.filename}")
        image = preprocess_image(file.read())  # Preprocess image

        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)  # Get class with highest probability
        result = CLASS_LABELS[predicted_class]   # Get class label

        print(f"🎯 Prediction: {result}")
        return jsonify({'result': result})
    except Exception as e:
        print(f"🔥 Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
