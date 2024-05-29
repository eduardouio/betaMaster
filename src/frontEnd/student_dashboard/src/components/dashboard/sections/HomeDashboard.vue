<script setup>
import TableStudents from '@/components/dashboard/TableStudents.vue';
import ModalStudent from '@/components/dashboard/ModalStudent.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';


const store = useStore();
let showModal = ref(false);
let idStudent = ref(0);
const cards = ['courses', 'students', 'schools']

const handleStudent = function(myId) {
    idStudent.value = myId;
    showModal.value = true;
    store.commit('enableLoader');
};

const closeModal = function() {
    store.commit('setNullStudentData');    
    showModal.value = false;
};

</script>
<template>
    <div>
        <div class="grid grid-cols-1 p-4 gap-4">
            <TableStudents @handleStudent="handleStudent($event)"/>
        </div>
        <ModalStudent v-if="showModal" :idStudent="idStudent" @closeModal="closeModal" />
    </div>
</template>
