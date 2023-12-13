<script setup>
  import NavBar from '../components/NavBar.vue';
  import { onMounted } from 'vue';

  onMounted(()=>{
    console.log('home Montado');
});

console.log('Mensaje de la plantilla Home');

</script>
<template>
  <div>
    <NavBar :itemSelected="'home'"/>
  
  </div>
</template>