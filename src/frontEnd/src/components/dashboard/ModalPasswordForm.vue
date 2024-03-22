<script setup>

import { XCircleIcon } from '@heroicons/vue/24/outline';

const emits = defineEmits(['handelModalPassword']);

function closeModal() {
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
            <div class="mt-4 bg-slate-100 border">  
                <div class="grid gap-1 text-sm grid-cols-1 md:grid-cols-3">
                    <label for="country col-1">
                      <strong class="text-red-500">*</strong>
                      Pais
                    </label>
                    <input type="text" class=" col-2 input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Apellidos" />
                </div>
            </div>
            <div class="modal-action">
                <form method="dialog">
                    <!-- if there is a button in form, it will close the modal -->
                    <button class="btn" @click="closeModal">Close</button>
                </form>
            </div>
        </div>
    </dialog>
</template>