<script setup>
import { ref, computed } from 'vue';
import { XCircleIcon, CheckCircleIcon, ExclamationCircleIcon } from '@heroicons/vue/24/outline';
import serverConfigData from '@/config';

const emits = defineEmits(['handelModalPassword','changePassword']);
let newPass = ref({
    password: '',
    confirmPassword: ''
});

const passwordMatch = computed(() => {
    if (newPass.value.password == '' || newPass.value.confirmPassword == '') {
        return false;
    }
    return newPass.value.password != newPass.value.confirmPassword;
});

const showBtnChangePassword = computed(() => {
    if (newPass.value.password == '' || newPass.value.confirmPassword == '') {
        return false;
    }
    return newPass.value.password === newPass.value.confirmPassword;
});

const changePassword = function() {
    emits('changePassword', newPass.value);
}

const handelModalPassword = function(){
    emits('handelModalPassword');
}

</script>
<template>
    <dialog id="my_modal_5" class="modal bg-gray-100/90 text-sm md:text-md" open="">
        <XCircleIcon @click="closeModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
        <div class="modal-box p-2 w-6/12 border rounded-md border-sky-600 border-l-8">
            <div class="flex">
                <span class="w-full inline-block text-center text-sm text-cyan-800">
                    Formulario De Cambio De Contraseña
                </span>
                <XCircleIcon @click="closeModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
            </div>
            <div class="h-30 md:h-10">
                <div v-if="passwordMatch" role="alert" class="flex p-2 rounded-xl bg-orange-400/80">
                    <ExclamationCircleIcon class="w-5 h-5" />
                    <span>Las contraseñas ingresadas no coinciden</span>
                </div>
            </div>
            <div class="mt-4">
                <div class="grid gap-1 text-sm grid-cols-2">
                    <label for="country col-1">
                        <strong class="text-red-500">*</strong>
                        Nueva Contraseña
                    </label>
                    <input type="password" v-model="newPass.password"
                        class=" col-2 input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="*******" />
                    <label for="country col-1">
                        <strong class="text-red-500">*</strong>
                        Repita Contraseña
                    </label>
                    <input type="password" v-model="newPass.confirmPassword"
                        class=" col-2 input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="*******" />
                </div>
            </div>
            <div class="modal-action">
                <form method="dialog" class="flex flex-col gap-4 md:flex-row md:gap-1">
                    <button v-if="showBtnChangePassword" class="btn btn-success btn-sm text-white"
                        @click="changePassword">
                        <CheckCircleIcon class="w-5 h-5 text-white" />
                        Actualizar Contraseña
                    </button>
                    <!-- if there is a button in form, it will close the modal -->
                    <button class="btn btn-primary btn-sm text-white" @click="handelModalPassword">
                        <XCircleIcon class="w-5 h-5 text-white" />
                        Close
                    </button>
                </form>
            </div>
        </div>
    </dialog>
</template>