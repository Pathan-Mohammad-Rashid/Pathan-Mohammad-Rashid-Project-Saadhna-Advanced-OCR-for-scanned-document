<template>
    <div>
        <h1>Urdu OCR System</h1>
        <input type="file" @change="uploadFile" />
        <p v-if="text"><strong>Extracted Text:</strong></p>
        <pre>{{ text }}</pre>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            text: '' // Extracted text from the backend
        };
    },
    methods: {
        async uploadFile(event) {
            const file = event.target.files[0];
            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await axios.post('http://localhost:8080/upload', formData);
                this.text = response.data.text;
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    }
};
</script>
