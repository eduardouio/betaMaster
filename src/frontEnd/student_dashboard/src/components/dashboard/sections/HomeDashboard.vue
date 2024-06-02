<script setup>
import TableStudents from '@/components/dashboard/TableStudents.vue';
import { computed, ref } from 'vue';
import { useStore } from 'vuex';
import { 
    UserCircleIcon, AcademicCapIcon, UserIcon
}      
from "@heroicons/vue/24/outline";
import serverConfigData from '@/config.js';


const store = useStore();
let showModal = ref(false);
let idStudent = ref(0);
const cards = ['courses', 'students', 'schools']

const handleStudent = function(myId) {
    idStudent.value = myId;
    showModal.value = true;
    store.commit('enableLoader');
};

const colorsStatus = {
    'PENDIENTE': 'bg-yellow-500',
    'APROBADO': 'bg-green-500',
    'RECHAZADO': 'bg-red-500',
}

const userData =  computed( () => store.getters.getProfile); 

// listado de cursos activos
const activeCourses = computed( () => {
    return store.getters.getCourses;
});

// imagen de perfirl seguún el sexo
const profilePic = computed( () => {
    if (store.getters.getPicture){
        return store.getters.getPicture;
    }

    if (userData.sex === 'FEMENINO'){
        return serverConfigData.imgs.picWomen;
    }
    return serverConfigData.imgs.picMen;
});

</script>
<template>
    <div class="bg-gray-100">
        <pre>
            {{courses}}
        </pre>
        <div class="container mx-auto my-5 p-5">
            <div class="md:flex no-wrap md:-mx-2 ">
                <!-- Left Side -->
                <div class="w-full md:w-3/12 md:mx-2">
                    <!-- Profile Card -->
                    <div class="bg-white p-3 hover:shadow">
                        <div class="flex items-center space-x-3 font-semibold text-gray-900 text-xl leading-8">
                        </div>
                        <div class="flex">
                            <div class="text-center my-2">
                                <img class="h-full w-full rounded-md mx-auto bg-cover" :src="store.getters.getPicture"
                                    :alt="userData.first_name + ' ' + userData.last_name">
                                    <img class="bg-login"/>
                            </div>
                        </div>
                    </div>
                    <div class="my-4"></div>
                    <div class="bg-white p-3 border-t-4 border-green-400">
                        <div class="image overflow-hidden">
                            <img class="h-auto w-full mx-auto"
                                :src="profilePic"
                                alt="">
                        </div>
                        <h1 class="text-gray-900 font-bold text-xl leading-8 my-1">{{ userData.first_name }} {{
                            userData.last_name }}</h1>
                        <h3 class="text-gray-600 font-lg text-semibold leading-6">
                            Nombre del Colegio
                        </h3>
                        <p class="text-sm text-gray-500 hover:text-gray-600 leading-6">
                            {{ userData.presentation }}
                        </p>
                        <ul
                            class="bg-gray-100 text-gray-600 hover:text-gray-700 hover:shadow py-2 px-3 mt-3 divide-y rounded shadow-sm">
                            <li class="flex items-center py-3">
                                <span>Status</span>
                                <span class="ml-auto">
                                    <span class="py-1 px-2 rounded text-white text-sm" :class="colorsStatus[userData.is_aproved]">
                                        {{ userData.is_aproved }}
                                    </span>
                                </span>
                            </li>
                            <li class="flex items-center py-3">
                                <span>Fecha de registro</span>
                                <span class="ml-auto" v-if="userData.date_aproved">
                                    {{ userData.date_aproved }}
                                </span>
                                <span class="ml-auto text-cyan-700" v-else >
                                    PENDIENTE
                                </span>
                            </li>
                        </ul>
                    </div>

                </div>
                <!-- Right Side -->
                <div class="w-full md:w-9/12 mx-2 h-64">
                    <!-- Profile tab -->
                    <!-- About Section -->
                    <div class="bg-white p-3 shadow-sm rounded-sm">
                        <div class="flex items-center space-x-2 font-semibold text-gray-900 leading-8">
                            <span clas="text-green-500">
                                <UserIcon class="h-5 w-5 text-lime-700" />
                            </span>
                            <span class="tracking-wide">Información Personal</span>
                        </div>
                        <div class="text-gray-700">
                            <div class="grid md:grid-cols-2 text-sm">
                                <div class="grid grid-cols-2">
                                    <div class="px-4 py-2 font-semibold">Género</div>
                                    <div class="px-4 py-2">{{ userData.sex }}</div>
                                </div>
                                <div class="grid grid-cols-2">
                                    <div class="px-4 py-2 font-semibold">Email</div>
                                    <div class="px-4 py-2">
                                        {{ userData.email }}
                                    </div>
                                </div>
                                <div class="grid grid-cols-2">
                                    <div class="px-4 py-2 font-semibold">Ciudad</div>
                                    <div class="px-4 py-2">{{ userData.state }} / {{ userData.city }} /
                                        {{ userData.parroquia }}</div>
                                </div>
                                <div class="grid grid-cols-2">
                                    <div class="px-4 py-2 font-semibold">Dirección</div>
                                    <div class="px-4 py-2">{{ userData.address }}</div>
                                </div>
                                <div class="grid grid-cols-2">
                                    <div class="px-4 py-2 font-semibold">Telefono</div>
                                    <div class="px-4 py-2">
                                        {{ userData.phone }}
                                    </div>
                                </div>
                                <div class="grid grid-cols-2">
                                    <div class="px-4 py-2 font-semibold">Fecha de Nacimiento</div>
                                    <div class="px-4 py-2">{{ userData.date_of_birth }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- End of about section -->

                    <div class="my-4"></div>

                    <!-- Experience and education -->
                    <div class="bg-white p-3 shadow-sm rounded-sm">
                        <div class="grid grid-cols-2">
                            <div>
                                <div class="flex items-center space-x-2 font-semibold text-gray-900 leading-8 mb-3">
                                    <span clas="text-green-500">
                                        <AcademicCapIcon class="h-5 w-5 text-lime-700" />
                                    </span>
                                    <span class="tracking-wide">Mis Cursos</span>
                                </div>
                                <ul class="list-inside space-y-2">
                                    <li v-for="course in activeCourses.active_courses" :key="course">
                                        <div class="text-teal-600">
                                            {{course.school.name}}
                                        </div>
                                        <div class="text-gray-500">
                                            {{ course.active_course.period }}
                                        </div>
                                        <div class="text-gray-500 text-xs">
                                            {{ course.active_course.state }}
                                        </div>
                                        <div class="text-gray-500 text-xs">
                                            {{ course.school.state }}
                                        </div>
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <div class="flex items-center space-x-2 font-semibold text-gray-900 leading-8 mb-3">
                                    <span clas="text-green-500">
                                       <UserCircleIcon class="h-5 w-5 text-lime-700" />
                                    </span>
                                    <span class="tracking-wide">Mis Profesores</span>
                                </div>
                                <ul class="list-inside space-y-2">
                                    <li>
                                        <div class="text-teal-600">Masters Degree in Oxford</div>
                                        <div class="text-gray-500 text-xs">March 2020 - Now</div>
                                        <div class="text-gray-500 text-xs">March 2020 - Now</div>
                                    </li>
                                    <li>
                                        <div class="text-teal-600">Bachelors Degreen in LPU</div>
                                        <div class="text-gray-500 text-xs">March 2020 - Now</div>
                                        <div class="text-gray-500 text-xs">March 2020 - Now</div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="grid grid-cols-2">
                            <div>
                                <div class="flex items-center space-x-2 font-semibold text-gray-900 leading-8 mb-3">
                                    <span clas="text-green-500">
                                        <AcademicCapIcon class="h-5 w-5 text-lime-700" />
                                    </span>
                                    <span class="tracking-wide">Cursos Concluidos</span>
                                </div>
                                <ul class="list-inside space-y-2">
                                    <li>
                                        <div class="text-teal-600">Owner at Her Company Inc.</div>
                                        <div class="text-gray-500 text-xs">March 2020 - Now</div>
                                    </li>
                                </ul>
                            </div>

                        </div>
                        <!-- End of Experience and education grid -->
                    </div>
                    <!-- End of profile tab -->
                </div>
            </div>
        </div>
    </div>

</template>
