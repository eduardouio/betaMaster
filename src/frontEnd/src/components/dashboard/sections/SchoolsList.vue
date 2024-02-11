<script setup>
import TableSchools from '@/components/dashboard/TableSchools.vue';
import ModalSchool from '@/components/dashboard/ModalSchool.vue';

import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';


const store = useStore();
let showModal = ref(false);
let idSchool = ref('0');

function handelModal() {
    showModal.value = false;
}

function handleIdSchool(id){
    idSchool.value = id.toString();
    showModal.value = true;
}
</script>

<template>
    <div>
        <TableSchools/>
        <ModalSchool/>
    </div>
</template>