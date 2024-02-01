<script setup>
import { RouterView } from 'vue-router';
import { onMounted, ref, shallowReactive } from 'vue';
import { useStore } from 'vuex';
import serverConfigData from '@/config';
import Footer from '@/components/Footer.vue';
import Loader from '@/components/generics/Loader.vue';
import SideBar from '@/components/dashboard/SideBar.vue';
import HeaderDashboard from '@/components/dashboard/HeaderDashboard.vue';  

let showLoader = ref(true);
const store = useStore();
let dashboardData = {};

onMounted(() => {
    document.title = 'Cargando Datos...';
    loadData();
});


// cargamos los datos del dashboard
async function loadData(){
    let url = serverConfigData.urls.teacherData.replace(
        '{idUser}', serverConfigData.idUser
    );
    let response = await fetch(
        url,{
        method: 'GET',
        headers: serverConfigData.headers
    });

    if(response.status != 200){
        console.log('Error al cargar los datos del dashboard');
        console.log(response);
    }else{        
        store.commit('setDashboardData', await response.json());
        dashboardData= await store.state.dashboardData;
        document.title = 'Resumen | Dashboard';
        showLoader.value = false;
    }
}
</script>
<template>
    <Loader v-if="showLoader" />
    <div v-else>
    <div class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-gray-700 text-black dark:text-white">
            <HeaderDashboard />
            <SideBar />
            <!--Contenido del dashboard-->
            <div class="h-full ml-14 mt-10 mb-10 md:ml-64 lg:pt-4 lg:pl-4 mr-2">
                <RouterView />
                <Footer />
            </div>
            <!--/Contenido del dashboard-->
        </div>
    </div>
</template>