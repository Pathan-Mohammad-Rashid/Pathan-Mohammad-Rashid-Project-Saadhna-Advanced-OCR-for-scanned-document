<template>
    <div id="app">
        <FileUpload />
    </div>
</template>

<script>
import FileUpload from './components/FileUpload.vue';

export default {
    components: {
        FileUpload
    }
};
</script>

<style>
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
}
</style>
