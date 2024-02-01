<script setup>
import { useStore } from 'vuex';
import { onMounted, ref } from 'vue';
import serverConfigData from '@/config';
import { ChevronDoubleLeftIcon, ChevronDoubleRightIcon, ChevronRightIcon, ChevronLeftIcon } from '@heroicons/vue/24/outline';

const store = useStore();
let dashboardData = store.state.dashboardData;
let paginatedData = ref([]);

let currentPage = ref(1);
let perPage = ref(10);
let offset = ref((currentPage.value - 1) * perPage.value);
let paginatedItems = ref(dashboardData.slice(offset.value).slice(0, perPage.value));


onMounted(() => {
    paginatedData.value = paginateContent(dashboardData);
});

function paginateContent(data) {
    let paginatedData = [];
    let page = 1;
    let perPage = 10;
    let offset = (page - 1) * perPage;
    let paginatedItems = data.slice(offset).slice(0, perPage);
    for (let i = 0; i < paginatedItems.length; i++) {
        paginatedData.push(paginatedItems[i]);
    }
    return paginatedData;
}


</script>
<template>
    <div
        class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words bg-gray-50 dark:bg-gray-800 w-full shadow-lg rounded">
        <div class="rounded-t mb-0 px-0 border-0">
            <div class="flex flex-wrap items-center px-4 py-2">
                <div class="relative w-full max-w-full flex-grow flex-1">
                    <h3 class="font-semibold text-base text-gray-900 dark:text-gray-50">Mis Estudiantes
                    </h3>
                </div>
                <div class="relative w-full max-w-full flex-grow flex-1 text-right">
                    <button class="text-sm text-primary btn btn-sm btn-outline">Ver Todo</button>
                </div>
            </div>
            <div class="block w-full overflow-x-auto">
                <table class="table table-border">
                    <thead>
                        <tr class="bg-gray-200 text-center text-gray-950">
                            <th>#</th>
                            <th>Estudiante</th>
                            <th>Colegio</th>
                            <th>Periodo</th>
                            <th>Estado</th>
                            <th>Ubicación</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="row,idx in paginateContent" class=" hover:bg-yellow-50" :key="row">
                            <td class="pb-0 pl-1">{{idx+1}}</td>
                            <td class="pb-0 pl-1">{{row.student.first_name}} {{row.student.last_name}}</td>
                            <td class="pb-0 pl-1">{{row.school.name}}</td>
                            <td class="pb-0 pl-1">{{row.active_course.period}}</td>
                            <td class="pb-0 pl-1">{{row.active_course.state}}</td>
                            <td class="pb-0 pl-1">{{row.student.city}}</td>
                        </tr>
                    </tbody>
                </table> 
                <section class="flex gap-2 p-2">
                    <button class="btn btn-xs btn-outline"><ChevronDoubleLeftIcon class="w-4 h-4"/></button>
                    <button class="btn btn-xs btn-outline"><ChevronLeftIcon class="h-4 w-4"/></button>
                    <button class="btn btn-xs btn-outline"><ChevronRightIcon class="h-4 w-4"/></button>
                    <button class="btn btn-xs btn-outline"><ChevronDoubleRightIcon class="h-4 w-4"/></button>
                </section>
            </div>
        </div>
    </div>
</template>