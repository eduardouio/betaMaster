<script setup>
import { useStore } from 'vuex';
import { onMounted, ref, watch } from 'vue';
import {    ChevronDoubleLeftIcon, ChevronDoubleRightIcon, 
            ChevronRightIcon, ChevronLeftIcon
        } from '@heroicons/vue/24/outline';
import serverConfigData from '@/config';

const classsStatus = {
    'POR INICIAR': 'text-xs text-sky-900',
    'EN PROCESO': 'text-xs text-green-900',
    'FINALIZADO': 'text-xs text-red-900'
};

const store = useStore();
const paginatedData = ref([]);
let listStudents = store.getters.getCourses;
let currentPage = ref(1);
let perPage = ref(10);
let filter = ref('');
let pages = ref(Math.ceil(listStudents / perPage.value));
let showingItems = ref(0);


const emits = defineEmits(['handleStudent']);
const handleStudent = (idStudent) => {
    emits('handleStudent', idStudent);
};

onMounted(() => { 
    paginateContent(listStudents);
});

watch(perPage, (newVal, oldVal) => {
    currentPage.value = 1;
    pages.value = Math.ceil(listStudents / perPage.value);
    paginateContent(listStudents);
});

watch(currentPage, (newVal, oldVal) => {
    if (newVal === -1) {
        currentPage.value = 1;
    } else if (newVal === -2) {
        currentPage.value = pages.value;
    }
    if (currentPage.value > pages.value) {
        currentPage.value = pages.value;
    }
    if (currentPage.value < 1) {
        currentPage.value = 1;
    }
    paginateContent(listStudents);
});

watch(filter, (newVal, oldVal) => {
    currentPage.value = 1;
    paginateContent(listStudents, newVal);
});

function paginateContent(data, filter = '') {
    if (filter) {
        data = filterData(data, filter);
    }
    let start = (currentPage.value - 1) * perPage.value;
    paginatedData.value = data.slice(start, start + perPage.value);
    showingItems.value = paginatedData.value.length;
}

function filterData(data, filter) {
    let filteredData = data.filter((item) => {
        return item.student.first_name.toLowerCase().includes(filter.toLowerCase()) ||
            item.student.last_name.toLowerCase().includes(filter.toLowerCase()) ||
            item.id_school.name.toLowerCase().includes(filter.toLowerCase()) ||
            item.period.toLowerCase().includes(filter.toLowerCase()) ||
            item.state.toLowerCase().includes(filter.toLowerCase()) ||
            item.student.city.toLowerCase().includes(filter.toLowerCase());
    });
    return filteredData;
}
</script>
<template>
    <div
        class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words bg-gray-50 dark:bg-gray-800 w-full shadow-lg rounded">
        <div class="rounded-t mb-0 px-0 border-0">
            <div class="flex flex-wrap items-center px-4 py-2">
                <div class="relative w-full max-w-full flex-grow flex-1">
                    <span class="text-gray-800">Mis Estudiantes
                    </span>
                </div>
                <div class="relative w-full max-w-full flex-grow flex-1 text-right">
                    <input type="text" class="input input-bordered input-xs" placeholder="buscar" v-model="filter">
                </div>
            </div>
            <div class="overflow-x-auto">
                <table class="table table-xs table-border 2xl:table-md">
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
                        <tr v-for="row, idx in paginatedData" class=" hover:bg-yellow-50" :key="row"
                            @click="handleStudent(row.student.id)">
                            <td class="pb-0 pl-1">{{ (perPage * (currentPage - 1)) + idx + 1 }}</td>
                            <td class="pb-0 pl-1">{{ row.student.first_name }} {{ row.student.last_name }}</td>
                            <td class="pb-0 pl-1">{{ row.id_school.name }}</td>
                            <td class="pb-0 pl-1">{{ row.period }}</td>
                            <td class="pb-0 pl-1">
                                <div :class="classsStatus[row.state]">
                                    {{ row.state }}
                                </div>
                            </td>
                            <td class="pb-0 pl-1">{{ row.student.city }}</td>
                        </tr>
                    </tbody>
                </table>
                <br />
                <hr>
                <div class="flex flex-wrap items-center px-4 py-2 bg-slate-100">
                    <div class="relative w-full max-w-full flex-grow flex-1 flex gap-1">
                        <button @click="currentPage = -1" class="btn btn-xs btn-outline text-gray-600">
                            <ChevronDoubleLeftIcon class="w-4 h-4" />
                        </button>
                        <button @click="currentPage--" class="btn btn-xs btn-outline text-gray-600">
                            <ChevronLeftIcon class="h-4 w-4" />
                        </button>
                        <button @click="currentPage++" class="btn btn-xs btn-outline text-gray-600">
                            <ChevronRightIcon class="h-4 w-4" />
                        </button>
                        <button @click="currentPage = -2" class="btn btn-xs btn-outline text-gray-600">
                            <ChevronDoubleRightIcon class="h-4 w-4" />
                        </button>
                    </div>
                    <div class="relative text-xs">
                        Página 1 de {{ pages }} - Mostrando {{ showingItems }} de {{ listStudents.length }} Registros
                    </div>
                    <div class="relative w-full max-w-full flex-grow flex-1 text-right">
                        <span class="text-xs">Elementos por Página </span>
                        <select class="select select-bordered select-xs" v-model="perPage">
                            <option value="10">10</option>
                            <option value="30">30</option>
                            <option value="60">60</option>
                            <option value="100">100</option>
                        </select>
                    </div>
                </div>
                <hr class="p-2">
            </div>
        </div>
    </div>
</template>