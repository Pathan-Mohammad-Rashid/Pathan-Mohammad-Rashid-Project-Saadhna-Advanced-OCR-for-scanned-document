# Project-Saadhna-Advanced-OCR-for-Scanned-Documents

# Reviving Urdu Heritage: Advanced OCR for Historical/Scanned Documents

Unlock the power of advanced OCR technology to preserve the rich Urdu literary heritage. This guide provides a step-by-step approach to building a robust OCR system using Vue.js for the frontend and Flask for the backend, leveraging Google Cloud's Vision API and Vertex AI for accurate Urdu text extraction.

## Introduction
The Urdu language, with its vast and rich literary history, is preserved in countless historical documents and manuscripts. However, many of these valuable resources are trapped in scanned or image formats, making it difficult to access their content. Traditional OCR systems often struggle to accurately recognize Urdu text due to the complexity of its script and the quality issues in older scans.

This project addresses this challenge by creating an advanced OCR system designed specifically for Urdu text extraction. By leveraging Google Cloud Vision API and UTRNet, this system extracts text with high accuracy, digitizing documents for future generations.

### Audience
This guide is designed for developers and data scientists interested in OCR technology, particularly those focusing on Urdu scripts and the integration of advanced AI services.

### Outcome
By the end of this project, you will have a fully functional OCR system with a Vue.js frontend for user interactions and a Flask backend for handling text extraction and processing.

---

## Design

### High-Level Architecture
The solution employs a hybrid approach, combining the general text detection capabilities of Google Cloud Vision API with the specialized Urdu text recognition of UTRNet.

#### Frontend (Vue.js):
- **User Interface:** A simple and intuitive UI that allows users to upload images or PDFs, view extracted text, and download results.
- **Components:** File upload, text display, and download options.

#### Backend (Flask):
- **API Endpoints:** Manages file uploads, processes OCR with Google Vision API, and performs post-processing with Vertex AI.
- **Data Storage:** Utilizes Google Cloud Storage for images and Firestore for text records.

#### Hybrid OCR Processing:
1. **Preprocessing:** Converts PDFs to images and enhances text visibility.
2. **Initial Text Detection:** Google Vision API detects text regions and layouts.
3. **Urdu Text Recognition:** UTRNet extracts Urdu text from the detected regions.
4. **Text Post-Processing:** Combines outputs and applies language-specific corrections.

### Rationale
- **Vue.js:** Provides a reactive and user-friendly interface for smooth interactions.
- **Flask:** Lightweight and flexible backend ideal for integration with Google Cloud services.
- **Google Vision API:** Efficient general text detection.
- **UTRNet:** High accuracy for Urdu script recognition.

---

## Prerequisites

### Software
- Node.js and npm
- Vue.js CLI
- Python 3
- Flask
- Google Cloud SDK

### Knowledge
- Basic understanding of Vue.js and Flask
- Familiarity with Google Cloud services (Vision API, Storage, Firestore)

---

## Step-by-Step Instructions

### Frontend Development with Vue.js
1. **Set Up Vue.js:**
   ```bash
   sudo apt-get install nodejs npm 
   npm install -g @vue/cli 
   vue create urdu-ocr-frontend 
   cd urdu-ocr-frontend 
   npm run serve
   ```
2. **Build the UI:**
   - Create components for file upload, text display, and download options.

3. **Install Axios for API Requests:**
   ```bash
   npm install axios
   ```

### Backend Development with Flask
1. **Set Up Flask App:**
   ```bash
   mkdir urdu-ocr-backend
   cd urdu-ocr-backend
   python3 -m venv venv
   source venv/bin/activate
   pip install Flask google-cloud-vision google-cloud-storage google-cloud-firestore
   ```
2. **Develop API Endpoints:**
   ```python
   from flask import Flask, request, jsonify
   from google.cloud import vision, storage, firestore

   app = Flask(__name__)

   # Initialize Google Cloud Clients
   vision_client = vision.ImageAnnotatorClient()
   storage_client = storage.Client()
   firestore_client = firestore.Client()

   @app.route('/upload', methods=['POST'])
   def upload_file():
       if 'file' not in request.files:
           return jsonify({'error': 'No file uploaded'}), 400
       
       file = request.files['file']
       bucket = storage_client.bucket('your-bucket-name')
       blob = bucket.blob(file.filename)
       blob.upload_from_file(file)

       image = vision.Image(source=vision.ImageSource(gcs_image_uri=f'gs://your-bucket-name/{file.filename}'))
       response = vision_client.text_detection(image=image)
       text = response.text_annotations[0].description if response.text_annotations else ''
       
       doc_ref = firestore_client.collection('documents').add({
           'filename': file.filename,
           'text': text
       })

       return jsonify({'text': text}), 200

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=8080)
   ```
3. **Testing Locally:**
   ```bash
   FLASK_APP=main.py flask run
   ```
   Use Postman or similar tools to test the API endpoints.

### Implementing Hybrid OCR Model

#### Preprocessing and Initial Text Detection:
```python
from google.cloud import vision, storage

# Detect text regions...
def detect_text_regions(image_path, bucket_name, blob_name):
    # Logic for text detection...
```

#### Urdu Text Recognition with UTRNet:
```python
import torch
from torchvision import transforms

# Model logic...
def recognize_urdu_text(region_image):
    # Text recognition logic...
```

#### Text Post-Processing:
```python
def post_process_text(urdu_text, vision_text):
    # Post-processing logic...
```

---

## Deployment

1. **Code in VS Code:** Write and organize your Python scripts, manage the environment, and execute the code.
2. **Google Cloud Console:** Set up services, manage billing, and view logs.
3. **Execution:** Test with your dataset and optimize the workflow.

---

## Result / Demo
The final system provides a user-friendly interface that allows users to upload images or PDFs, extract Urdu text, and download results.

- **GitHub Repository:** [Project Saadhna OCR](https://github.com/Pathan-Mohammad-Rashid/Project-Saadhna-Advanced-OCR-for-Scanned-Documents.git)
- **Demo Link:** [Demo](https://drive.google.com/drive/folders/1kh4W1A63TYMnNvxEvH-OKE6DK9Zbf_HF?usp=sharing)

---

## What's Next?
Explore related topics and projects:
- Advanced OCR Techniques
- Integrating AI with Cloud Services
- Improving Text Recognition Accuracy

---

# Tags
#OCRTechnology #UrduLiterature #DigitalPreservation #VueJS #Flask #GoogleCloud #VisionAPI #VertexAI #ArtificialIntelligence #MachineLearning #CloudComputing #UrduHeritage
