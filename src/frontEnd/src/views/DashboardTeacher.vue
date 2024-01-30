<script setup>
import {onMounted } from 'vue';
import {useStore} from 'vuex';
import { RouterView } from 'vue-router';
import serverConfigData from '../config';

import SideBar from '../components/dashboard/SideBar.vue';
import HeaderDashboard from '../components/dashboard/HeaderDashboard.vue';
import Loader from '../components/generics/Loader.vue';

const store = useStore();




</script>

<template>
    <div>
    <div class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-gray-700 text-black dark:text-white">
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