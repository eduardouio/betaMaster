<script setup>
import TableStudents from '@/components/dashboard/TableStudents.vue';
import { computed, getCurrentInstance, onMounted, ref } from 'vue';
import { useStore } from 'vuex';
import { 
    UserCircleIcon, AcademicCapIcon, UserIcon, 
    DevicePhoneMobileIcon, EnvelopeIcon, MapPinIcon
}      
from "@heroicons/vue/24/outline";
import serverConfigData from '@/config.js';


const store = useStore();
let showModal = ref(false);
let idStudent = ref(0);
const cards = ['courses', 'students', 'schools']
const currentCourse = ref(null);
const UrlMapBase = 'https://www.google.com/maps/?q=';

const handleStudent = function(myId) {
    idStudent.value = myId;
    showModal.value = true;
    store.commit('enableLoader');
};

const colorsStatus = {
    'PENDIENTE': 'bg-yellow-500',
    'APROBADO': 'bg-green-500',
    'RECHAZADO': 'bg-red-500',
    'EN PROCESO': 'text-green-700',
    'FINALIZADO': 'text-gray-700',
    'POR INICIAR': 'text-yellow-700',

}



onMounted(() => {
    currentCourse.value = getCurrentCourse();
});

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

// obtenemos el curso activo
const getCurrentCourse = () => {
    const activeCourses =  store.getters.getCourses.active_courses.filter(
        course => {
        return  course.active_course.state === 'EN PROCESO'
    });
    if (activeCourses.length > 0){
        return activeCourses[0];
    }
    return null;
};

const getImage = (teacher) => {
    if (teacher.picture){
        return teacher.picture;
    }

    if (teacher.sex === 'FEMENINO'){
        return serverConfigData.imgs.picWomen;
    }

    return serverConfigData.imgs.picMen;
};

</script>
<template>
    <div class="bg-gray-100">
        <div class="container mx-auto my-5 p-5">
            <div class="md:flex no-wrap md:-mx-2 ">
                <!-- Left Side -->
                <div class="w-full md:w-3/12 md:mx-2">
                    <!-- Profile Card -->
                    <div class="bg-white p-3 hover:shadow">
                        <div class="flex items-center space-x-3 font-semibold text-gray-900 text-xl leading-8">
                        </div>
                        <div class="flex justify-center text-xl">
                            {{ userData.first_name }} {{ userData.last_name }}
                        </div>
                    </div>
                    <div class="my-4"></div>
                    <div class="bg-white p-3 border-t-4 border-green-400">
                        <div class="image overflow-hidden border-b-2 pb-4">
                            <img class="h-auto w-full mx-auto" :src="profilePic" alt="">
                        </div>
                        <h3 class="text-gray-600 font-lg text-semibold leading-6 text-info m-2 text-xl">
                            <span v-if="currentCourse">
                                {{ currentCourse.school.name }}
                            </span>
                            <span v-else>
                                NO TIENE CURSO ACTIVO
                            </span>
                        </h3>
                        <p class="text-sm text-gray-500 hover:text-gray-600 leading-6 ">
                            {{ userData.presentation }}
                        </p>
                        <ul
                            class="bg-gray-100 text-gray-600 hover:text-gray-700 hover:shadow py-2 px-3 mt-3 divide-y rounded shadow-sm">
                            <li class="flex items-center py-3">
                                <span>Status</span>
                                <span class="ml-auto">
                                    <span class="py-1 px-2 rounded text-white text-sm"
                                        :class="colorsStatus[userData.is_aproved]">
                                        {{ userData.is_aproved }}
                                    </span>
                                </span>
                            </li>
                            <li class="flex items-center py-3">
                                <span>Fecha Aprovación</span>
                                <span class="ml-auto text-cyan-700">
                                    <span v-if="userData.date_aproved">
                                        {{ userData.date_aproved.toLocaleDateString('es-EC') }}
                                    </span>
                                    <span v-else>
                                        NO REGISTRA
                                    </span>
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
                                            {{ course.school.name }}
                                        </div>
                                        <div class="text-gray-500">
                                            {{ course.active_course.period }}
                                        </div>
                                        <div class="text-gray-500 text-xs font-bold"
                                            :class="colorsStatus[course.active_course.state]">
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
                                <div v-if="currentCourse">
                                    <ul class="list-inside space-y-2" v-for="teacher in currentCourse.teachers"
                                        :key="teacher">
                                        <li class="text-teal-600 flex flex-col gap-1 border-b p-2">
                                            <div class="flex items-center gap-2">
                                                <img :src="getImage(teacher)" alt="Imagen de Profesor" class="w-1/12">
                                                {{ teacher.first_name }} {{ teacher.last_name }}
                                                /
                                                <MapPinIcon class="h-4 w-4 text-cyan-700" />
                                                <a class="text-cyan-700" target="_blank" rel="noreferrer"
                                                    :href="UrlMapBase + teacher.geolocation.toString()">
                                                    Mapa
                                                </a>
                                                /
                                                <span class="text-gray-500">
                                                    {{ teacher.city }}
                                                </span>
                                            </div>
                                            <div class="flex items-center gap-2">
                                                <div class="text-sm">
                                                <a :href="'tel:' + teacher.phone" class="text-info flex">
                                                    <DevicePhoneMobileIcon class="h-4 w-4 text-lime-700" />
                                                    {{ teacher.phone }}
                                                </a>
                                            </div>
                                            /
                                            <div class="flex items-center gap-2">
                                                <EnvelopeIcon class="h-4 w-4 text-lime-700" />
                                                <a :href="'mailto:' + teacher.email">
                                                    {{ teacher.email }}
                                                </a>
                                            </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div v-else>
                                    NO REGISTRA UN CURSO ACTIVO
                                </div>
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
