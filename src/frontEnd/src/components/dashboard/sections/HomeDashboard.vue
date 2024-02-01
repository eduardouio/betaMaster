<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableSchools from '@/components/dashboard/TableSchools.vue';
import TableCandidates from '@//components/dashboard/TableCandidates.vue';
import { useStore } from 'vuex';

const store = useStore();
const dashboardData = store.state.dashboardData;

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
            <TableSchools/>
        </div>
    </div>
</template>
