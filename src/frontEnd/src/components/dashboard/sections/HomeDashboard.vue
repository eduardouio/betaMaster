<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableStudents from '@/components/dashboard/TableStudents.vue';
import ModalStudent from '@/components/dashboard/ModalStudent.vue';
import { useStore } from 'vuex';
import { ref } from 'vue';

const store = useStore();
let showModal = ref(false);
let idStudent = ref('0');
</script>
<template>
    <div>
        <div class="grid items-center grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 ">
            <CardIndicator :nameCard="'courses'"/>
            <CardIndicator :nameCard="'students'"/>
            <CardIndicator :nameCard="'schools'"/>
        </div>
        <div class="grid grid-cols-1 p-4 gap-4">
            <TableStudents/>
        </div>
        <ModalStudent v-if="showModal" :idStudent="idStudent" @closeModal="handelModal"/>
    </div>
</template>
