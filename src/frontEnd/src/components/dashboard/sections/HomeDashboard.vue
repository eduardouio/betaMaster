<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableSchools from '@/components/dashboard/TableSchools.vue';
import ModalStudent from '@/components/dashboard/ModalStudent.vue';
import { useStore } from 'vuex';
import { ref } from 'vue';

const store = useStore();
const dashboardData = store.state.dashboardData;
let showModal = ref(false);
let idStudent = ref('0');

function handleIdStudent(id){
    idStudent.value = id.toString();
    showModal.value = true;
};

function handelModal(){
    showModal.value = false;
}

</script>
<template>
    <div>
        <div class="grid items-center grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 ">
            <CardIndicator 
            :nameCard="'Cursos'" 
            :totalCard="dashboardData.length" 
            />
            <CardIndicator 
            :nameCard="'Estudiantes'" 
            :totalCard="dashboardData.length" 
            />
            <CardIndicator 
            :nameCard="'Colegios'" 
            :totalCard="dashboardData.length" 
            />
        </div>
        <div class="grid grid-cols-1 p-4 gap-4">
            <TableSchools
            @idStudent="handleIdStudent"
            />
        </div>
        <ModalStudent 
            v-if="showModal" 
            :idStudent="idStudent"
            @closeModal="handelModal"
            />
    </div>
</template>
