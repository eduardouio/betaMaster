<script setup>
import { useStore } from 'vuex';
import { onMounted, ref } from 'vue';
import serverConfigData from '@/config';

let showLoader = ref(true);
const store = useStore();
let dashboardData = store.state.dashboardData;
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
                        <tr class="bg-gray-100 text-center">
                            <th>#</th>
                            <th>Estudiante</th>
                            <th>Curso</th>
                            <th>Colegio</th>
                            <th>Ciudad</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="row,idx in dashboardData" class="text-gray-700 hover:bg-yellow-50" :key="row">
                            <td>{{idx+1}}</td>
                            <td>{{row.student.first_name}} {{row.student.last_name}}</td>
                            <td>{{row.school.name}}</td>
                            <td>{{row.active_course.period}}</td>
                            <td>{{row.active_course.state}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>