<template>
    <div class="toast">
        <div :class="classToast" class="text-white">
            <ul>
                <li v-for="error in statusMessage" :key="error.type">
                    {{error.typeError}}: {{error.message}}
                </li>   
            </ul>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue';
const classToast = ref('');
const statusMessage = ref([]);

const props = defineProps(
    {
        typeToast: String,
        statusResponse: Object,
    }
);

const toastTypes = {
    error: 'alert alert-error',
    success: 'alert alert-success',
    warning: 'alert alert-warning',
    info: 'alert alert-info',
};

onMounted(() => {
    if (props.statusResponse.status.is_success) {

        classToast.value = toastTypes.success;
        statusMessage.value = [
            {
                typeError: 'OK',
                message: 'Operacion completada con éxito!'
            }
        ]
        return;
    }

    const errors = Object.keys(props.statusResponse.status.response);
    if (errors.length > 0) {
        statusMessage.value = errors.map((error) => {
            return {
                typeError: error,
                message: props.statusResponse.status.response[error][0]
            }
            ;
        });
    } 

    classToast.value = toastTypes.error;
});

</script>