<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableStudents from '@/components/dashboard/TableStudents.vue';
import ModalStudent from '@/components/dashboard/ModalStudent.vue';
import { ref } from 'vue';


let showModal = ref(false);
let idStudent = ref(0);
const cards = ['courses', 'students', 'schools']

const handleStudent = function(myId) {
    idStudent.value = myId;
    showModal.value = true;
};

const closeModal = function() {
    showModal.value = false;
};

</script>
<template>
    <div>
        <div class="grid items-center grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 ">
            <CardIndicator 
                v-for="card in cards" 
                :nameCard="card" 
                :key="card"
            />
        </div>  
        <div class="grid grid-cols-1 p-4 gap-4">
            <TableStudents @handleStudent="handleStudent($event)"/>
        </div>
        <ModalStudent v-if="showModal" :idStudent="idStudent" @closeModal="closeModal" />
    </div>
</template>
