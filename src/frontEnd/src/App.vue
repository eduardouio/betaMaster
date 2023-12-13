<script setup>
import { RouterLink } from 'vue-router';
import HomeView from './views/HomeView.vue';
import RegisterView from './views/RegisterView.vue';
import Footer from './components/Footer.vue';
</script>
<template>
    <div>
        <RouterView />
        <Footer/>
    </div>
</template>
