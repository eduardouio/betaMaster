<script setup>
import { ref } from 'vue';
import { XCircleIcon ,ArrowUpTrayIcon, PhotoIcon} from '@heroicons/vue/24/outline';

let image = ref(null);
let urlImage = ref('');
const emits = defineEmits(['handelModalPicture', 'changePicture']);

const closeModal = function(){
    emits('handelModalPicture');
}

const showImage = function(e){
    image = e.target.files[0];
    urlImage.value = URL.createObjectURL(image);
};

const handelModalPicture = function(){
    emits('changePicture',  image);
}
</script>
<template>
    <dialog id="my_modal_6" class="modal bg-gray-100/90 text-sm md:text-md" open="">
        <XCircleIcon @click="closeModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
        <div class="modal-box p-2 w-6/12 border rounded-md border-sky-600 border-l-8">
            <div class="flex">
                <span class="w-full inline-block text-center text-sm text-cyan-800">
                    Formulario De Cambio de Imagen Perfil
                </span>
                <XCircleIcon @click="closeModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
            </div>
            <div class="mt-4">
                <div class="flex justify-center h-[12rem] w-full rounded-md border p-3">
                    <img
                        v-if="urlImage"
                        class="h-full w-auto rounded-md border border-gray-300" 
                        :src="urlImage"
                        alt="Shoes"
                    />
                </div>
                <div class="grid gap-1 text-sm grid-cols-2 mt-5">
                    <label for="country col-1">
                        <div class="flex gap-3">
                            Seleccione una imagen 
                            <PhotoIcon class="w-5 h-5 text-cyan-600"/>
                        </div>
                        </label>
                    <input
                        @change="showImage"
                        type="file"
                        accept="image/*"
                        class="col-2 input input-sm input-secondary focus:input-primary w-full md:h-11"
                        />
                </div>
            </div>
            <div class="modal-action">
            <form method="dialog" class="flex flex-col gap-4 md:flex-row md:gap-1">
                <button class="btn btn-success btn-sm text-white" @click="handelModalPicture">
                    <ArrowUpTrayIcon class="w-5 h-5 text-white" />
                    Subir Imagen
                </button>
                <button class="btn btn-primary btn-sm text-white" @click="closeModal">
                        <XCircleIcon class="w-5 h-5 text-white" />
                        Cerrar
                </button>
            </form>
        </div>
        </div>
    </dialog>
</template>