<script setup>
import { onMounted, ref, watch } from 'vue';
import { useStore } from 'vuex';
import 
    { 
        ChevronDoubleLeftIcon,
        ChevronDoubleRightIcon,
        ChevronRightIcon,
        ChevronLeftIcon,
		MapPinIcon
    } 
from '@heroicons/vue/24/outline';
import serverConfigData from '@/config';
import LoaderVue from '@/components/generics/Loader.vue';

// emitimos el id del colegio
const emits = defineEmits(['idSchool']);
function emitIdSchools(id){
	emits('idSchool', id);

}

// listamos colegios unicos
const seen = new Set();
const collegesList = ref([]);
const store = useStore();
const paginatedData = ref([]);
// defimimos los emits para actualizar el modal
let filter = ref('');
let pages = ref(0);
let currentPage = ref(1);
let perPage = ref(10);
let showingItemsTable = ref(0);
let showLoader = ref(false);

function paginateContent(data, filter='') {
	if (filter) {
        data = filterData(data, filter);
    }
	let start = (currentPage.value - 1) * perPage.value;

	paginatedData.value = data.slice(start, start + perPage.value);
	showingItemsTable.value = paginatedData.value.length;
}

// filtro de datos
function filterData(data, filter) {
	
    let filteredData = data.filter((item) => {
        return item.name.toLowerCase().includes(filter.toLowerCase()) || 
        item.state.toLowerCase().includes(filter.toLowerCase()) || 
        item.city.toLowerCase().includes(filter.toLowerCase()) || 
        item.ami_code.toLowerCase().includes(filter.toLowerCase()) || 
        item.address.toLowerCase().includes(filter.toLowerCase());
    });
    return filteredData;
}

onMounted(async() => {
	const dashboardData = await store.state.dashboardData;
	document.title = 'Colegio | Dashboard';
	collegesList.value = dashboardData.map((item) => {
		return item.school;
	}).filter((val) => {
		if (seen.has(val.id)) {
			return false;
		}
		seen.add(val.id);
		return true;
	});
	pages.value = Math.ceil(collegesList.value.length / perPage.value);
	paginateContent(collegesList.value);
});

// miramos si tenemos el filtro
watch(filter, (newVal, oldVal) => {
    currentPage.value = 1;
    paginateContent(collegesList.value, newVal);
});

// miramos la cantidad de registros por pagina
watch(perPage, (newVal, oldVal) => {
    currentPage.value = 1;
    pages.value = Math.ceil(collegesList.value.length / perPage.value);
    paginateContent(collegesList.value);
});

// miramos la pagina actual
watch(currentPage, (newVal, oldVal) => {
    if (newVal === -1) {
        currentPage.value = 1;
    } else if (newVal === -2) {
		currentPage.value = Math.ceil(collegesList.value.length / perPage.value);
    }
    if (currentPage.value > pages.value) {
        currentPage.value = pages.value;
    }
    if (currentPage.value < 1) {
        currentPage.value = 1;
    }
    paginateContent(collegesList.value);
});

</script>
<template>
    <div
        class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words bg-gray-50 dark:bg-gray-800 w-full shadow-lg rounded">
        <div class="rounded-t mb-0 px-0 border-0">
            <div class="flex flex-wrap items-center px-4 py-2">
                <div class="relative w-full max-w-full flex-grow flex-1">
                    <h3 class="text-gray-900">Mis Instituciones Educativas
                    </h3>
                </div>
                <div class="relative w-full max-w-full flex-grow flex-1 text-right">
                    <input type="text" class="input input-bordered input-xs" placeholder="buscar" v-model="filter">

                </div>
            </div>
            <div class="block w-full overflow-x-auto">
                <table class="table table-border">
                    <thead>
                        <tr class="bg-gray-200 text-center text-gray-950">
                            <th>#</th>
                            <th>Colegio</th>
							<th>Codigo AMI</th>
                            <th>Contacto</th>
                            <th>Provincia</th>
                            <th>Ubicación</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="row, idx in paginatedData" class=" hover:bg-yellow-50" :key="row"
                            click="emitIdStudent(row.student.id)">
                            <td class="pb-0 pl-1"> {{(perPage * (currentPage - 1)) + idx + 1 }}</td>
                            <td class="pb-0 pl-1"> <small class="text-gray-500">(#{{ row.id }})</small> {{row.name}}</td>
							<td class="pb-0 pl-1"> {{row.ami_code}}</td>
                            <td class="pb-0 pl-1"> {{row.email }}</td>
                            <td class="pb-0 pl-1"> {{row.state }}, {{row.city }}</td>
                            <td class="pb-0 pl-1"> <MapPinIcon class="w-4 h-4 inline-block text-info"/> {{row.address }}</td>
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
                        Página 1 de  pages }} - Mostrando  showingItemsTable }} de  dashboardData.length }} Registros
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