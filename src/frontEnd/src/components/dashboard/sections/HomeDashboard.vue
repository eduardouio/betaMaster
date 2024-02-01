<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableSchools from '@/components/dashboard/TableSchools.vue';
import TableCandidates from '@//components/dashboard/TableCandidates.vue';
</script>
<template>
    <div>
        <div class="grid items-center grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 ">
            <CardIndicator 
            :nameCard="'Cursos'" 
            :totalCard="12" 
            />
            <CardIndicator 
            :nameCard="'Estudiantes'" 
            :totalCard="34" 
            />
            <CardIndicator 
            :nameCard="'Colegios'" 
            :totalCard="23" 
            />
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 p-4 gap-4">
            <TableSchools />
            <TableCandidates />
        </div>
    </div>
</template>
