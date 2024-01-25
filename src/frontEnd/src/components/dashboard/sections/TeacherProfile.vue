<script setup>
import { RouterLink } from 'vue-router';
import { useStore } from 'vuex';
import { CheckBadgeIcon, CogIcon, NewspaperIcon } from '@heroicons/vue/24/outline';
import serverConfigData from '../../../config.js';

import SocialIcon from '../../generics/SocialIcon.vue';

const store = useStore();
let userData = store.getters.getUserData;
let roleUser = {
    teacher: 'Docente Educativo',
    student: 'Estuidante',
    school: 'Institución Educativa',
};

const formatDate = ((my_date) => {
    if (!my_date) {
        return '';
    }
    let date = new Date(my_date);
    return date.toLocaleDateString(
        'es-EC', { year: 'numeric', month: 'long', day: 'numeric' }
    );
});

const timeLapsed = ((my_date, years = true) => {
    if (!my_date) {
        return '';
    }
    let date = new Date(my_date);
    let today = new Date();
    let age = today.getFullYear() - date.getFullYear();
    let m = today.getMonth() - date.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < date.getDate())) {
        age--;
    }
    if (years) {
        return `${age} Años`
    }
    let lapsed = Math.abs(age * 12 + m);
    return `${lapsed} Meses`;
});
</script>
<template>
    <div>
        <div class="bg-gradient-to-b from-gray-50 to-slate-100 rounded-lg shadow-xl p5-8 pt-10 mr-4">
            <div class="w-full h-[30px] bg-gradient-to-l from-slate-600 to-slate-500"></div>
            <div class="flex flex-col items-center -mt-20 border">
                <img :src="userData.picture" class="w-40 border-4 border-white rounded-full">
                <div class="flex items-center space-x-2 mt-2">
                    <p class="text-2xl">{{ userData.first_name }} {{ userData.last_name }}</p>
                    <span class="bg-blue-500 rounded-full p-1" title="Verified">
                        <CheckBadgeIcon class="h-5 w-5 text-white" aria-hidden="true" />
                    </span>
                </div>
                <p class="text-gray-700">{{ roleUser[userData.role] }}</p>
                <button class="btn btn-sm btn-primary text-white mb-2">
                    <RouterLink to="/dashboard-teacher/edit">
                        <CogIcon class="w-5 h-5 inline-block" /> Modificar Perfil
                    </RouterLink>
                </button>
            </div>
        </div>
        <div class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
            <div class="w-full flex flex-col 2xl:w-3/5">
                <div class="flex-1 bg-white rounded-lg shadow-xl p-7">
                    <h4 class="text-xl text-gray-900 font-bold">Información Personal</h4>
                    <ul class="mt-2 text-gray-700">
                        <li class="flex border-y py-2">
                            <span class="font-bold w-2/5">Nombres:</span>
                            <span class="text-gray-700">{{ userData.first_name }} {{ userData.last_name }}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">F Nacimiento:</span>
                            <span class="text-gray-700">{{ formatDate(userData.date_of_birth) }} <small
                                    class="text-slate-600">({{ timeLapsed(userData.date_of_birth) }})</small></span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Joined:</span>
                            <span class="text-gray-700">{{ formatDate(userData.date_joined) }}<small
                                    class="text-slate-600">({{ timeLapsed(userData.date_joined,
                                        years = false) }})</small></span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Celular:</span>
                            <span class="text-gray-700">{{ userData.phone }}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Email:</span>
                            <span class="text-gray-700">{{ userData.email }}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Ubicación:</span>
                            <span class="text-gray-700">{{ userData.state }}, {{ userData.city }} <br> {{ userData.address
                            }}</span>
                        </li>
                        <li class="flex items-center border-b py-2 space-x-2">
                            <span class="font-bold w-2/5">Mis Redes:</span>
                            <SocialIcon :url="userData.url_facebook" :icon="'facebook'" />
                            <SocialIcon :url="userData.url_linkedin" :icon="'linkedin'" />
                            <SocialIcon :url="userData.url_instagram" :icon="'instagram'" />
                            <SocialIcon :url="userData.url_twiter" :icon="'twitter'" />
                        </li>
                    </ul>
                </div>
            </div>
            <div class="flex flex-col w-full 2xl:w-2/3">
 

                <div class="flex-1 bg-white rounded-lg shadow-xl p-8">
                    <h4 class="text-xl text-gray-900 font-bold">Mi Presentación</h4>
                    <div class="mt-2 text-gray-900" v-html="userData.presentation">
                    </div>
                    <button class="btn btn-sm btn-primary text-white mb-1 mt-1">
                        <NewspaperIcon class="w-5 h-5 inline-block" />
                        Hoja de Vida
                    </button>
                </div>

            </div>
        </div>
        <div class="bg-white rounded-lg shadow-xl p-8">
            <div class="flex items-center justify-between">
                <h4 class="text-xl text-gray-900 font-bold">Estudiantes (12)</h4>
            </div>
            <div
                class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-8 gap-8 mt-8">
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection1.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Diane Aguilar</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection1.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Diane Aguilar</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection3.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Carlos Friedrich</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection4.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Donna Serrano</p>
                    <p class="text-xs text-gray-500 text-center">System Engineer at Tesla</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection5.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Randall Tabron</p>
                    <p class="text-xs text-gray-500 text-center">Software Developer at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection6.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">John McCleary</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection7.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Amanda Noble</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection8.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Christine Drew</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection9.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Lucas Bell</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection10.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Debra Herring</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection11.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Benjamin Farrior</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection12.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Maria Heal</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection13.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Edward Ice</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection14.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Jeffery Silver</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection15.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Jennifer Schultz</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection16.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Joseph Marlatt</p>
                    <p class="text-xs text-gray-500 text-center">General Basica</p>
                    <p class="text-xs text-gray-500 text-center">Coelgio 24 de Mayo</p>
                </a>
            </div>
        </div>
    </div>
</template>
