<script setup>
import { RouterView } from 'vue-router';
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import Footer from '@/components/Footer.vue';
import Loader from '@/components/generics/Loader.vue';
import SideBar from '@/components/dashboard/SideBar.vue';
import HeaderDashboard from '@/components/dashboard/HeaderDashboard.vue';  

const store = useStore();
const isLoading = computed(() => store.getters.getIsLoading);

const stagesLoaded = computed(() => {
    if (store.getters.getStagesLoaded === 8) {
        store.commit('setIsLoading', false);
        return true;
    }
    return false;
});

onMounted(() => {
    store.dispatch('fetchProfile');
    store.dispatch('fetchBankAccounts');
    store.dispatch('fetchReferences');
    store.dispatch('fetchSchools');
    store.dispatch('fetchStudents');
    store.dispatch('fetchCourses');
    store.dispatch('fetchProfileFile', 'picture');
    store.dispatch('fetchProfileFile', 'cv');
});

</script>
<template>
    <div>
    <Loader v-if="isLoading" />
    <div v-if="stagesLoaded">
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
    <div v-else class="text-info">
        Cargando datos... 
        {{ store.getters.getStagesLoaded     }}
    </div>
</div>
</template>