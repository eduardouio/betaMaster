<script setup>
import { useStore, mapGetters } from 'vuex';
import { ref } from 'vue';
import { CheckIcon, PencilSquareIcon, XCircleIcon, XMarkIcon } from '@heroicons/vue/24/outline';

const store = useStore();
const userData = store.state.userData;
let showForm = ref(true);

</script>
<template>
<div>
    <div v-if="showForm" class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div class="row">
            <label for="enterprise">Empresa</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>
        <div class="row">
            <label for="enterprise">Fecha Incio</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>
        <div class="row">
            <label for="enterprise">Fecha Fin</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>  
        <div class="row">
            <label for="enterprise">Contacto</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>
        <div class="row">
            <label for="enterprise">Relación</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>
        <div class="row">
            <label for="enterprise">Tipo Referencia</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>
        <div class="row">
            <label for="enterprise">Correo</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>  
        <div class="row">
            <label for="enterprise">Teléfono</label>
            <input type="text" id="enterprise" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
        </div>  

    </div>
    <table v-else class="table table-xs">
        <!-- head -->
        <thead class="text-gray-600">
            <tr>
                <th>#</th>
                <th>Emisor</th>
                <th>Tipo</th>
                <th>Contacto</th>
                <th>Estado</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(exp, idx) in userData.references" :key="exp">
                <td>{{ idx + 1 }}</td>
                <td>{{ exp.enterprise }}</td>
                <td>{{ exp.type }}</td>
                <td>{{ exp.name_contact }}</td>
                <td nowrap>
                    <span class="flex gap-2">
                        <CheckIcon v-if="exp.is_verified" class="w-5 h-5 text-success" />
                        <XCircleIcon v-else class="w-5 h-5 text-error" />
                        <span v-if="exp.is_verified">Verificado</span>
                        <span v-else>Pendiente</span>
                    </span>
                </td>
                <td>
                    <span class="flex items-center gap-2">
                        <PencilSquareIcon class="w-5 h-5 text-primary" />
                        <XMarkIcon class="w-5 h-5 text-error" />
                    </span>
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>