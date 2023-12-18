<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableSchools from '../TableSchools.vue';
import TableCandidates from '../TableCandidates.vue';
</script>
<template>
    <div>
        <div class="grid grid-cols-1 grid-cols-2 gap-10 ">
            <CardIndicator />
            <CardIndicator />
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 p-4 gap-4">
            <TableSchools />
            <TableCandidates />
        </div>
    </div>
</template> 