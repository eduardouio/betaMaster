<script setup>
import { RouterLink } from 'vue-router';
import { useStore } from 'vuex';
import Loader from '../../generics/Loader.vue';
import { computed, reactive, onMounted, ref } from 'vue';
import {
    CheckBadgeIcon, CogIcon, NewspaperIcon, MapPinIcon, FolderArrowDownIcon,
    XMarkIcon, CheckIcon, PencilSquareIcon
} from '@heroicons/vue/24/outline';
import serverConfigData from '../../../config.js';
import SocialIcon from '../../generics/SocialIcon.vue';

let showLoader = ref(true);
const store = useStore();
let userData = {};

onMounted(() => {
    console.log('montado dashboard');
    getUserData();
});

// recuperamos los datos del usuario y lo colocamos en el store
async function getUserData() {
    let url = serverConfigData.urls.getUser.replace(
        '{idUser}', serverConfigData.idUser
    );
    let response = await fetch(url, {
        method: 'GET',
        headers: serverConfigData.headers
    });

    if (response.status != 200) {
        console.log('Error al cargar los datos del dashboard');
        console.log(response);
    } else {
        store.commit('setUserData', await response.json());
        userData = await store.state.userData;
        showLoader.value = false;
    }
}


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
    let url = '';
    if (!userData.geolocation) {
        return url;
    }
    let coordinates = userData.geolocation.split(',');
    url = `https://www.google.com/maps/?q=${coordinates[0]},${coordinates[1]}`;
    return url;
});

const formatDate = ((my_date) => {
    if (!my_date) {
        return '';
    }
    let date = new Date(my_date);
    return date.toLocaleDateString(
        'es-EC', { year: 'numeric', month: 'long', day: 'numeric' }
    );
});

const profilePic = computed(() => {
    if (userData.picture) {
        return userData.picture;
    }
    if (userData.sex === 'male') {
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
        <Loader class="mx-auto" v-if="showLoader.value" />
        <div v-else>
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
                    <br />
                    <button class="btn btn-sm btn-primary text-white mb-2">
                        <RouterLink to="/dashboard-teacher/edit">
                            <CogIcon class="w-5 h-5 inline-block" /> Modificar Perfil
                        </RouterLink>
                    </button>
                </div>
            </div>
            <div role="tablist" class="tabs tabs-lifted mt-4">
                <a role="tab" class="tab" :class="tabList.personal_data ? 'tab-active tb-active' : ''"
                    @click="changeTab('personal_data')">
                    Datos Personales
                </a>
                <a role="tab" class="tab" :class="tabList.references ? 'tab-active tb-active' : ''"
                    @click="changeTab('references')">
                    Referencias/Experiencia
                </a>
                <a role="tab" class="tab" :class="tabList.bank_data ? 'tab-active tb-active' : ''"
                    @click="changeTab('bank_data')">
                    Información Bancaria
                </a>
            </div>
            <!--tab profile-->
            <div v-if="tabList.personal_data" class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
                <div class="w-full flex flex-col 2xl:w-3/5">
                    <div class="flex-1 bg-white rounded-lg shadow-xl p-7">
                        <ul class="text-gray-700">
                            <li class="flex border-y py-2">
                                <span class="font-bold w-2/5">Nombres:</span>
                                <span class="text-gray-700">
                                    <div class="tooltip" data-tip="Descargar Hoja de Vida" v-if="userData.cv">
                                        <a :href="userData.cv">
                                            <FolderArrowDownIcon class="w-5 h-5 inline-block text-info" />
                                        </a>
                                    </div>
                                    {{ userData.first_name }} {{ userData.last_name }}
                                    <small v-if="userData.profesion" class="badge badge-outline badge-neutral">{{
                                        userData.profesion }}</small>

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
                                <span class="text-gray-700">{{ userData.phone }} <span class="text-gray-300">|</span> {{
                                    userData.phone_2 }}</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Email:</span>
                                <div class="tooltip"
                                    :data-tip="userData.is_confirmed_mail ? 'Correo Confirmado' : 'Sin Confirmar'"
                                    :class="!userData.is_confirmed_mail ? 'tooltip-error' : ''">
                                    <span class="text-gray-700">{{ userData.email }}
                                        <CheckBadgeIcon v-if="userData.is_confirmed_mail"
                                            class="w-5 h-5 inline-block text-success" />
                                    </span>
                                </div>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Ubicación:</span>
                                <span class="text-gray-700">{{ userData.state }}, {{ userData.city }} <br> {{
                                    userData.address
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
                                    <a :href="geolocation" target="_blank">
                                        <MapPinIcon class="w-6 h-6 text-primary" />
                                    </a>
                                    {{ userData.state }}, {{ userData.city }}, {{ userData.address }}
                                </section>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Nacionalidad:</span>
                                <span class="text-gray-700">{{ userData.nationality }} <small
                                        class="text-gray-300">|</small> {{ userData.civil_status }}</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Nro Cedula:</span>
                                <span class="text-gray-700">{{ userData.dni_number }}</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Nivel Educativo:</span>
                                <span class="text-gray-700 uppercase">{{ userData.level_education }}</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Discapacidad:</span>
                                <span class="text-gray-700">{{ userData.have_disability ? 'SI' : 'NO' }}
                                    <small v-if="userData.have_disability" class="badge bg-cyan-50">{{
                                        userData.type_disability }} {{ userData.disability_persent }}% Carnet:{{
        userData.card_conadis }}</small>
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
            <!--/tab profile-->
            <!--tab references-->
            <div v-if="tabList.references" class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
                <table class="table border">
                    <!-- head -->
                    <thead>
                        <tr class="bg-gray-100 text-center">
                            <th>#</th>
                            <th>Tipo</th>
                            <th>Empresa</th>
                            <th>Contacto</th>
                            <th>Inicio</th>
                            <th>Fin</th>
                            <th>Estado</th>
                            <th>
                                <CogIcon class="w-5 h-5" />
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(reference, idx) in userData.references" :key="reference.id_reference"
                            class="hover:bg-yellow-50">
                            <td>{{ idx + 1 }}</td>
                            <td>{{ reference.type }}</td>
                            <td>{{ reference.enterprise }}</td>
                            <td>
                                {{ reference.name_contact }}
                                <small class="badge bg-cyan-50">{{ reference.relationship }}</small>
                            </td>
                            <td>{{ reference.start_date }}</td>
                            <td>{{ reference.end_date }}</td>
                            <td class="text-center">
                                <CheckIcon v-if="reference.is_verified" class="w-5 h-5 inline-block text-success" />
                                <XMarkIcon v-else class="w-5 h-5 inline-block text-error" />
                            </td>
                            <td>
                                <PencilSquareIcon class="w-5 h-5 inline-block text-primary" />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <!--/tab references-->
            <!--tab bank data-->
            <div v-if="tabList.bank_data" class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
                <table class="table border">
                    <!-- head -->
                    <thead>
                        <tr class="bg-slate-300 text-center">
                            <th>#</th>
                            <th>Banco</th>
                            <th>Nro de Cuenta</th>
                            <th>Tipo</th>
                            <th>Titular</th>
                            <th>Correo</th>
                            <th>Estado</th>
                            <th>
                                <CogIcon class="w-5 h-5" />
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(account, idx) in userData.accounts" :key="account.id_bank" class="hover:bg-yellow-50">
                            <td>{{ idx + 1 }}</td>
                            <td>{{ account.bank_name }}</td>
                            <td>{{ account.nro_account }}</td>
                            <td>{{ account.type_account }}</td>
                            <td>
                                {{ account.owner_name }}
                                <small class="badge bg-cyan-50">{{ account.owner_dni }}</small>
                        </td>
                        <td>{{ account.email_notify }}</td>
                        <td class="text-center">
                            <CheckIcon v-if="account.is_verified" class="w-5 h-5 inline-block text-success" />
                            <XMarkIcon v-else class="w-5 h-5 inline-block text-error" />
                        </td>
                        <td>
                            <PencilSquareIcon class="w-5 h-5 inline-block text-primary" />
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!--/tab bank data-->
    </div>
</div></template>
