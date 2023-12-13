<script setup>
import { onMounted } from 'vue';
import NavBar from '../components/NavBar.vue';
import UserRegister from '../components/UserRegister.vue';


onMounted(()=>{
    console.log('register Montado');
});

console.log('Mensaje de la plantilla Registro');

</script>

<template>
    <div>
      <NavBar :itemSelected="'register'"/>
      <UserRegister/>
    </div>
</template>
  