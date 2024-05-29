<script setup>
import TableSchools from '@/components/dashboard/TableSchools.vue';
import ModalSchool from '@/components/dashboard/ModalSchool.vue';

import { ref } from 'vue';
let showModal = ref(false);

function handelModal() {
    showModal.value = false;
}
let school = {};

function handelSchool(mySchool){
    school = mySchool;
    showModal.value = true;
}   
</script>

<template>
    <div>
        <TableSchools @school="handelSchool"  />
        <ModalSchool v-if="showModal"  :school="school" @closeModal="handelModal"/>
    </div>
</template>