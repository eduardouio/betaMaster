<script setup>
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import { ref } from 'vue';

const showLogin = ref(true);

const handelForm = () => {
    console.log('cambio de formulario');
    showLogin.value = !showLogin.value;
}
</script>
<template>
    <div>
        <Login v-if="showLogin" @changeForm="handelForm"/>
        <Register @changeForm="handelForm" v-else/>
    </div>
</template>