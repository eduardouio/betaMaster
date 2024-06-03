<script setup>
import { useStore } from 'vuex';
import { computed, onMounted, ref, watch } from 'vue';
import {    ChevronDoubleLeftIcon, ChevronDoubleRightIcon, 
            ChevronRightIcon, ChevronLeftIcon, DevicePhoneMobileIcon,
            MapPinIcon, XCircleIcon
        } from '@heroicons/vue/24/outline';
import serverConfigData from '@/config';
import SocialIcon from '@/components/generics/SocialIcon.vue';

const store = useStore();
const paginatedData = ref([]);
const listStudents = ref([])
let currentPage = ref(1);
let perPage = ref(10);
let filter = ref('');
let pages = ref(0);
let showingItems = ref(0);
const UrlMapBase = 'https://www.google.com/maps/?q=';

const emits = defineEmits(['handleStudent']);
const handleStudent = (idStudent) => {
    emits('handleStudent', idStudent);
};

onMounted(() => {
    listStudents.value = store.getters.getTeachers;
    pages = Math.ceil(listStudents.value.length / perPage.value)
    paginateContent(listStudents);
});

watch(perPage, (newVal, oldVal) => {
    currentPage.value = 1;
    pages.value = Math.ceil(listStudents.value / perPage.value);
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

function getPic(teacher) {
    if (teacher.picture){
        return teacher.picture;
    }

    if (teacher.sex === 'FEMENINO'){
        return serverConfigData.imgs.picWomen;
    }

    return serverConfigData.imgs.picMen;
};

function paginateContent(data, filter = '') {
    data  = data.value;
    if (filter) {
        data = filterData(data, filter);
    }
    let start = (currentPage.value - 1) * perPage.value;
    paginatedData.value = data.slice(start, start + perPage.value);
    showingItems.value = paginatedData.value.length;
}

function filterData(data, filter) {
    let filteredData = data.filter((item) => {
        if (!item.state){item.state = '';}
        if (!item.city){item.city = '';}
        return item.first_name.toLowerCase().includes(filter.toLowerCase()) ||
            item.last_name.toLowerCase().includes(filter.toLowerCase()) ||
            item.state.toLowerCase().includes(filter.toLowerCase()) ||
            item.city.toLowerCase().includes(filter.toLowerCase());
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
                            <th>Nombres</th>
                            <th>Ubicación</th>
                            <th>Correo</th>
                            <th>Profesión</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="row, idx in paginatedData" class=" hover:bg-yellow-50" :key="row"
                            @click="handleStudent(row.id)">
                            <td class="pb-0 pl-1 w-[50px]">
                                <div class="flex gap-1">
                                {{ (perPage * (currentPage - 1)) + idx + 1 }}
                                <img :src="getPic(row)" :alt="'Profesor' + row.last_name + row.first_name">
                            </div>
                            </td>
                            <td class="pb-0 pl-1">
                                <div class=" flex items-center">
                                <div class="flex items-center justify-start gap-3 p-1 w-7/12 xl:w-6/12">
                                    <SocialIcon v-if="row.url_facebook" url="row.url_facebook" icon="facebook" />
                                    <XCircleIcon v-else class="w-5 h-5 text-gray-300" />
                                    <SocialIcon v-if="row.url_twiter" url="row.url_twiter" icon="twitter" />
                                    <XCircleIcon v-else class="w-5 h-5 text-gray-300" />
                                    <SocialIcon v-if="row.url_linkedin" url="row.url_linkedin" icon="linkedin" />
                                    <XCircleIcon v-else class="w-5 h-5 text-gray-300" />
                                </div>      
                                {{ row.first_name }} {{ row.last_name }} 
                            </div>
                            </td>
                            <td class="pb-0 pl-1">
                                <div class="flex gap-2">
                                <span>{{ row.state }}</span>
                                <span class="font-sm text-gray-300">/</span>
                                <span>{{ row.city }}</span>
                                <a :href="UrlMapBase + String(row.geolocation)" target="_blank">
                                    <MapPinIcon class="w-4 h-4 text-red-600" />
                                </a>
                            </div>
                            </td>
                            <td class="pb-0 pl-1">
                                {{ row.email }}
                            </td>
                            <td class="pb-0 pl-1">
                                {{ row.profesion }}
                                <div class="flex items-center">
                                        {{ item }}
                            </div>
                            </td>
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
                    <div class="relative text-xs" v-if="listStudents">
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