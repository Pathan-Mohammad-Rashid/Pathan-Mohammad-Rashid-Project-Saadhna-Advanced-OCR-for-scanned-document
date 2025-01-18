# Advanced OCR for Scanned Documents (Project Saadhna)

An advanced Optical Character Recognition (OCR) system built to extract Urdu text from scanned documents or images. The system uses a Vue.js frontend for user interaction and a Flask backend to process files via Google Cloud's Vision API. This project digitizes Urdu text for better access and preservation of its rich literary heritage.

## Motivation

Urdu is one of the most beautiful and complex scripts, but many of its historic and cultural documents remain trapped in image or scanned formats. Existing OCR systems often fail to properly recognize Urdu due to its unique script style. This project is an attempt to create a basic but functional OCR system tailored for Urdu text extraction, using modern cloud technologies.

## Features

- **File Upload**: Upload images or scanned documents (e.g., .jpg, .png, .pdf).
- **Text Extraction**: Automatically extract text using Google Cloud Vision API.
- **Real-Time Preview**: See the extracted Urdu text displayed on the webpage.
- **Firestore Integration**: Save the extracted text in Google Firestore for later use.

## Technologies Used

- **Frontend**: Vue.js
- **Backend**: Flask (Python)
- **Cloud Services**:
  - Google Cloud Vision API (for OCR)
  - Google Cloud Storage (for storing uploaded files)
  - Google Cloud Firestore (for saving extracted text)

## Deployment:

- **Backend**: Google App Engine
- **Frontend**: Netlify or Vercel

## System Architecture

1. User uploads an image through the Vue.js frontend.
2. The image is sent to the Flask backend.
3. The backend:
   - a) Uploads the image to Google Cloud Storage.
   - b) Passes the image to the Google Cloud Vision API for OCR.
   - c) Saves the extracted text to Google Firestore.
4. The extracted text is returned to the Vue.js frontend and displayed to the user.

## Setup Instructions

### Prerequisites

Make sure you have the following installed and set up:

- Python 3.7+
- Node.js and npm
- Google Cloud Account with:
  - Vision API enabled.
  - A Cloud Storage bucket created.
  - A Firestore database set up in Native Mode.
  - A Google Cloud Service Account Key downloaded as a JSON file.

### Backend Setup (Flask)

1. Clone this repository and navigate to the backend folder:

    ```bash
    git clone https://github.com/your-username/urdu-ocr-system.git
    cd urdu-ocr-system/urdu-ocr-backend
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Add your Google Cloud Service Account Key to the backend folder:

    - Save the key file as `service_account_key.json`.
    - Update the Cloud Storage bucket name in `app.py`:

    ```python
    bucket_name = 'your-bucket-name'
    ```

4. Start the backend server:

    ```bash
    python app.py
    ```

The backend will run on http://localhost:8080.

### Frontend Setup (Vue.js)

1. Navigate to the frontend folder:

    ```bash
    cd ../urdu-ocr-frontend
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm run serve
    ```

The frontend will run on http://localhost:8080.

4. Update the API endpoint in `FileUpload.vue`:

    ```javascript
    const response = await axios.post('http://localhost:8080/upload', formData);
    ```

## How to Use

1. Start both the backend and frontend as described above.
2. Open the frontend in your browser (http://localhost:8080).
3. Upload an Urdu document or image (e.g., .jpg, .png, or .pdf).
4. Wait for the extracted text to appear on the page.
5. Copy the extracted text or save it for later use.

## Deployment

### Backend Deployment (Google App Engine)

1. Navigate to the `urdu-ocr-backend` folder:

    ```bash
    cd urdu-ocr-backend
    ```

2. Deploy the Flask app to Google App Engine:

    ```bash
    gcloud app deploy
    ```

   Note the deployed URL (e.g., https://<your-project-id>.appspot.com).

3. Update the API endpoint in the frontend to use this URL:

    ```javascript
    const response = await axios.post('https://<your-project-id>.appspot.com/upload', formData);
    ```

### Frontend Deployment (Netlify or Vercel)

1. Navigate to the `urdu-ocr-frontend` folder:

    ```bash
    cd ../urdu-ocr-frontend
    ```

2. Build the Vue.js app:

    ```bash
    npm run build
    ```

3. Deploy the `dist/` folder to:
   - **Netlify**: Drag and drop the `dist/` folder into the Netlify dashboard.
   - **Vercel**: Use the Vercel CLI or dashboard to deploy.

## Screenshots

- **File Upload UI**
![Screenshot 2024-07-29 212858](https://github.com/user-attachments/assets/6e925105-d505-48f0-9078-19af83e89272)

## Future Improvements

- **Better OCR Model**: Integrate models like UTRNet or other custom-trained Urdu OCR models for higher accuracy.
- **Batch Processing**: Allow multiple file uploads at once.
- **Output Formats**: Provide an option to download the extracted text in PDF, Word, or Text formats.
- **Improved UI**: Add loading indicators and error messages for a better user experience.

## Contributors

This project was developed as part of a personal learning initiative. Contributions and suggestions are always welcome!

## License

This project is licensed under the MIT License. Feel free to use, modify, or share this project for your own needs.
