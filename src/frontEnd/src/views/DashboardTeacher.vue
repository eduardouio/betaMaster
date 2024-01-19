<script setup>
import {onMounted } from 'vue';
import {useStore} from 'vuex';
import { RouterView } from 'vue-router';
import serverConfigData from '../config';

import SideBar from '../components/dashboard/SideBar.vue';
import HeaderDashboard from '../components/dashboard/HeaderDashboard.vue';
import Loader from '../components/generics/Loader.vue';

const store = useStore();
const showLoader = false;

onMounted(() => {
    console.log('montado dashboard');
    getUserData();
});

// recuperamos los datos del usuario y lo colocamos en el store
async function getUserData(){
    let url = serverConfigData.urls.getUser.replace(
        '{idUser}', serverConfigData.idUser
    );
    let response = await fetch(url, {
        method: 'GET',
        headers: serverConfigData.headers
    });
    
    if (response.status !=200){
        alert('Error al obtener los datos del usuario');
    }else{
        store.commit('setUserData', await response.json());
    }
}
</script>

<template>
    <div>
    <Loader v-if="showLoader"/>
    <div v-if="!showLoader" class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-gray-700 text-black dark:text-white">
            <HeaderDashboard />
            <SideBar />
            <!--Contenido del dashboard-->
            <div class="h-full ml-14 mt-14 mb-10 md:ml-64 lg:pt-4 lg:pl-4">
                <RouterView />
            </div>
            <!--/Contenido del dashboard-->
        </div>
    </div>
</template>