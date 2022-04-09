<template>
<div class="upload container">
    <h2>The Form</h2>
    <UploadForm/>
 </div>

</template>
<script>
import UploadForm from "../components/UploadForm.vue";
export default {
    data() {
    return {};
    },
    components: { UploadForm }
};

</script>
<style>
.hide{
    visibility: hidden;
}

.show{
    visibility: visible;
}
</style>