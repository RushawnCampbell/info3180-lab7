<template>
     <span id="msg" class=" form-control alert" >
     </span>
    <form @submit.prevent="uploadPhoto" method="POST" id="uploadForm" >
        <div class="form-group">
            <label for="description">description</label>
            <textarea class="form-control" id="description" rows="3" name="description" ></textarea>
        </div>

        <div class="form-group">
            <label for="photo">photo</label>
            <input type="file" class="form-control-file" id="photo"  name="photo" >
        </div>

         <input type="submit" class="btn btn-primary"/>
         
    </form>
</template>

<script>
    export default {

        data() {
            return {
                
                csrf_token: ''
            };
        },
        methods: {
            uploadPhoto (){
                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm);
                let self = this;
                let alertcontainer =  document.querySelector('span#msg');
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
                    alertcontainer.classList.remove('hide');
                    if (Array.isArray(data)){
                        alertcontainer.innerHTML = '';
                        self.errorlist = data;
                        alertcontainer.classList.remove('alert-success');
                        alertcontainer.classList.add('alert-danger');
                        let errorlist = data;
                        for (let err=0; err<errorlist.length; err++){
                            const erroritem = document.createElement("li");
                            const node = document.createTextNode(errorlist[err]);
                            erroritem.appendChild(node);
                            alertcontainer.appendChild(erroritem);
                        }
                       
                    }
                    else{
                        alertcontainer.classList.add('alert-success');
                        alertcontainer.classList.remove('alert-danger');
                        alertcontainer.innerHTML= data.message;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
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
                
        },
        created() {
            this.getCsrfToken();
        }
}
</script>

<style>

form *{
    margin-bottom: 1em;
}

</style>