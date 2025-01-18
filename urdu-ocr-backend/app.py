from flask import Flask, request, jsonify
from google.cloud import vision, storage, firestore
import os

app = Flask(__name__)

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account_key.json'

# Initialize Google Cloud Clients
vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()
firestore_client = firestore.Client()

# File upload and text recognition endpoint
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    # Save file to Cloud Storage
    file = request.files['file']
    bucket_name = 'your-bucket-name'
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    # Perform OCR with Vision API
    image = vision.Image(source=vision.ImageSource(gcs_image_uri=f'gs://{bucket_name}/{file.filename}'))
    response = vision_client.text_detection(image=image)
    text = response.text_annotations[0].description if response.text_annotations else 'No text detected.'

    # Save the text in Firestore
    firestore_client.collection('documents').add({
        'filename': file.filename,
        'text': text
    })

    # Return the text as JSON
    return jsonify({'text': text}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
