<script setup>
import { useStore } from 'vuex';
import { onMounted, ref } from 'vue';
import { 
    CheckIcon, PencilSquareIcon, XCircleIcon, XMarkIcon, PlusCircleIcon,
    FolderArrowDownIcon
} from '@heroicons/vue/24/outline';
import serverConfigData from '@/config';

const store = useStore();
const references = store.getters.getReferences;
const showForm = ref(false);

const deleteReferece = function (idx) {
    store.dispatch('deleteReference', idx);
};
const types = {
    'references': ['PERSONAL', 'PROFESSIONAL', ],
    'relationships': [
        'FAMILIAR', 'JEFE INMEDIATO'    , 'COMPAÑERO DE TRABAJO', 'OTRO',
    ],
}
const addReference = function () {
    showForm.value = !showForm.value;
};

const currentReference = ref();

onMounted(() => {
    resetReference();
});

const setReference = function(reference){
    currentReference.value = reference;
    showForm.value = true;

};

const resetReference = function(){
    currentReference.value = {
        id_reference:0,
        id_user:serverConfigData.idUser,
        type:'',
        enterprise:'',
        start_date:'',
        end_date:'',
        name_contact:'',
        relationship:'',
        is_verified:false,
        is_active:true,
        phone_contact:'',
        email_contact:'',
    }
};

</script>
<template>
<div>
    <div class="flex justify-between items-center p-2">
        <button v-if="!showForm"  @click="showForm = !showForm" class="btn btn-sm bg-lime-600 text-white">
            <PlusCircleIcon class="w-5 h-5" />
            Agregar Referencia
        </button>
        <button v-else @click="addReference" class="btn btn-sm bg-slate-600 text-white">
            <FolderArrowDownIcon class="w-5 h-5" />
            Guardar Referencia
        </button>
        <button v-if="showForm" @click="showForm = !showForm" class="btn btn-sm bg-orange-600 text-white">
            <XCircleIcon class="w-5 h-5" />
            Cancelar
        </button>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4" v-if="showForm">
        <div class="row">
            <label for="enterprise">Empresa</label>
            <input 
                type="text" 
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.enterprise"
            />
        </div>
        <div class="row">
            <label for="enterprise">Fecha Incio</label>
            <input 
                type="text"
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.start_date"
            />
        </div>
        <div class="row">
            <label for="enterprise">Fecha Fin</label>
            <input
                type="text"
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.end_date"
            />
        </div>  
        <div class="row">
            <label for="enterprise">Contacto</label>
            <input
                type="text"
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.name_contact"
            />
        </div>
        <div class="row">
            <label for="enterprise">Relación</label>
            <select
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.relationship"
            >
                <option value="">Seleccione</option>
                <option  v-for="op in types.relationships" :value="op" :key="op">{{ op }}</option>
            </select>
        </div>
        <div class="row">
            <label for="enterprise">Tipo Referencia</label>
            <select 
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.type"
            >   
                <option value="">Seleccione</option>
                <option  v-for="op in types.references" :value="op" :key="op">{{ op }}</option>
            </select>
        </div>
        <div class="row">
            <label for="enterprise">Correo</label>
            <input
                type="text"
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.email_contact"
            />
        </div>  
        <div class="row">
            <label for="enterprise">Teléfono</label>
            <input
                type="text"
                class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                v-model="currentReference.phone_contact"
            />
        </div>  
    </div>
    <table class="table table-xs" v-else>
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
            <tr v-for="(exp, idx) in references" :key="exp">
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
                        <PencilSquareIcon class="w-5 h-5 text-primary" @click="setReference(exp)"/>
                        <XMarkIcon class="w-5 h-5 text-error" />
                    </span>
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>