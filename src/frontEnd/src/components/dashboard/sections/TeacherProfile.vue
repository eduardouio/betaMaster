<script setup>
import { RouterLink } from 'vue-router';
import { useStore } from 'vuex';
import { 
    CheckBadgeIcon, CogIcon, NewspaperIcon, MapPinIcon, FolderArrowDownIcon
} from '@heroicons/vue/24/outline';
import serverConfigData from '../../../config.js';

import SocialIcon from '../../generics/SocialIcon.vue';
import { computed, reactive } from 'vue';

const store = useStore();
let userData = store.getters.getUserData;
let roleUser = {
    teacher: 'Docente Educativo',
    student: 'Estuidante',
    school: 'Institución Educativa',
};

const tabList = reactive({
    personal_data: true,
    references: false,
    bank_data: false
});

function changeTab(tabName) {
    Object.keys(tabList).forEach((key) => {
        tabList[key] = tabName === key;
    });
}

// Computed properties
const geolocation = computed(() => {
    let coordinates = userData.geolocation.replace('(','').replaceAll(')','').replaceAll('\'', '').split(',');
    let url = `https://www.google.com/maps/?q=${coordinates[0]},${coordinates[1]}`;
    return url;
});

const civil_status = {
    single: 'Soltero',
    married: 'Casado',
    divorced: 'Divorciado',
    widowed: 'Viudo',
    separated: 'Separado',
    free_union: 'Unión Libre',
    other: 'Otro',
};

const level_education = {
    primary: 'Primaria',
    secundary: 'Secundaria',
    superior: 'Superior',
    Postgrado: 'Postgrado',
    master: 'Master',
    doctor: 'Doctorado',
    other: 'Otro',
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

const profilePic = computed(()=>{
    if (userData.picture) {
        return userData.picture;
    }
    if (userData.sex === 'male'){
        return '/src/assets/profile-pic-men.png';
    }
    return '/src/assets/profile-pic-women.png';
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
            <div class="w-full h-[30px] bg-gradient-to-l from-blue-100 to-cyan-100 border"></div>
            <div class="flex flex-col items-center -mt-20 border">
                <img :src="profilePic" class="w-40 border-4 border-white rounded-full">
                <div class="flex items-center space-x-2 mt-2">
                    <p class="text-2xl">{{ userData.first_name }} {{ userData.last_name }} 
                        
                        </p>
                    <span class="bg-blue-500 rounded-full p-1" title="Verified">
                        <CheckBadgeIcon class="h-5 w-5 text-white" aria-hidden="true" />
                    </span>
                </div>
                <p class="text-gray-700 text-md text-center ">{{ userData.presentation }}</p>
                <br/>
                <button class="btn btn-sm btn-primary text-white mb-2">
                    <RouterLink to="/dashboard-teacher/edit">
                        <CogIcon class="w-5 h-5 inline-block" /> Modificar Perfil
                    </RouterLink>
                </button>
            </div>
        </div>
        <div role="tablist" class="tabs tabs-lifted mt-4">
            <a role="tab" class="tab" :class="tabList.personal_data?'tab-active tb-active':''" @click="changeTab('personal_data')">
                Datos Personales
            </a>
            <a role="tab" class="tab" :class="tabList.references?'tab-active tb-active':''" @click="changeTab('references')">
                Referencias/Experiencia
            </a>
            <a role="tab" class="tab" :class="tabList.bank_data?'tab-active tb-active':''" @click="changeTab('bank_data')">
                Informacion Bancarias
            </a>
        </div>
        <div class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
            <div class="w-full flex flex-col 2xl:w-3/5">
                <div class="flex-1 bg-white rounded-lg shadow-xl p-7">
                    <ul class="text-gray-700">
                        <li class="flex border-y py-2"> 
                            <span class="font-bold w-2/5">Nombres:</span>
                            <span class="text-gray-700">
                                <div class="tooltip" data-tip="Descargar Hoja de Vida" v-if="userData.cv"> 
                                    <a :href="userData.cv">
                                        <FolderArrowDownIcon class="w-5 h-5 inline-block text-info"/>
                                    </a>
                                </div>
                                {{ userData.first_name }} {{ userData.last_name }}
                                <small v-if="userData.profesion" class="badge badge-outline badge-neutral">{{ userData.profesion }}</small>
                                
                            </span>
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
                            <span class="text-gray-700">{{ userData.phone }} <span class="text-gray-300">|</span> {{ userData.phone_2 }}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Email:</span>
                            <div class="tooltip" :data-tip="userData.is_confirmed_mail?'Correo Confirmado':'Sin Confirmar'" :class="!userData.is_confirmed_mail?'tooltip-error':''">
                            <span class="text-gray-700">{{ userData.email }}
                                    <CheckBadgeIcon v-if="userData.is_confirmed_mail" class="w-5 h-5 inline-block text-success" />
                                </span>
                            </div>
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
            <div class="w-full flex flex-col 2xl:w-3/5">
                <div class="flex-1 bg-white rounded-lg shadow-xl p-7">
                    <ul class="text-gray-700">
                        <li class="flex items-center border-y py-2">
                            <span class="font-bold w-2/5">Ubicación:</span>
                            <section class="text-gray-700 flex">
                                <a :href="geolocation" target="_blank"><MapPinIcon class="w-6 h-6 text-primary" /></a>
                                {{ userData.state }}, {{ userData.city}}, {{ userData.address }}
                            </section>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Nacionalidad:</span>
                            <span class="text-gray-700">{{ userData.nationality }} <small class="text-gray-300">|</small> {{ civil_status[userData.civil_status] }}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Nro Cedula:</span>
                            <span class="text-gray-700">{{ userData.dni_number}}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Nivel Educativo:</span>
                            <span class="text-gray-700">{{ level_education[userData.level_education] }}</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Discapacidad:</span>
                            <span class="text-gray-700">{{ userData.have_disability?'SI':'NO' }} 
                                <small v-if="userData.have_disability" class="text-info">{{ userData.type_disability }} {{ userData.disability_persent }}% {{ userData.card_conadis }}</small>
                            </span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-2/5">Último Acceso:</span>
                            <span class="text-gray-700">{{ formatDate(userData.last_login) }}</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
