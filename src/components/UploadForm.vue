<template>
    <form @submit.prevent="uploadPhoto" method="post" enctype="multipart/form-data" id="uploadForm">
        <label for="photo">Upload your photo here:</label>
        <input type="file" name="photo" id="photo" required>

        <label for="description">Enter description here:</label>
        <textarea name="description" id="description" cols="50" rows="4" required></textarea>

        <button type="submit">Submit Photo</button>
    </form>
</template>

<script>
    export default{
        name: "uploadForm",
        data(){
            return{ 
                csrf_token: ''
            }
        },
        created() {
            this.getCsrfToken();
        },
        methods:{
            uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            let self = this
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
            }
        }
    }
    
</script>