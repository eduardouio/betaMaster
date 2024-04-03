<script setup>
  import NavBar from '../components/NavBar.vue';
  import { onMounted } from 'vue';
  import headerImage from '@/assets/images/header-image.svg';
  import 'animate.css';

</script>
<template>
    <div>
        <NavBar />
        <div id="home" class="container mx-auto header_hero bg-gray relative z-10 overflow-hidden lg:flex items-center">    
            <div class=" bg-black border" style="padding: 2rem;">
                <div class="row">
                    <div class="w-full lg:w-1/2">
                        <div class="header_hero_content pt-150 lg:pt-0">
                            <h2
                                class="hero_title text-2xl sm:text-4xl md:text-5xl lg:text-4xl xl:text-5xl font-light text-white">
                                Bienvenidos a 
                                <span class="text-theme-color">Academy Learning Group</span></h2>
                            <p class="mt-8 lg:mr-8 text-xl text-white">en 
                                <strong>Academy Learning Group</strong>
                                creemos firmemente en la individualidad del aprendizaje y en el poder de la educación personalizada. Nos complace presentar una nueva forma de educación: el Homeschooling de la mano de expertos. 
                            </p>
                            <div class="hero_btn mt-10">
                                <a class="main-btn border" href="/#services">Quiero Comenzar</a>
                            </div>
                        </div> <!-- header hero content -->
                    </div>
                </div> <!-- row -->
            </div> <!-- container -->
            <div class="header_shape hidden lg:block"></div>

            <div class="header_image flex items-center">
                <div class="image 2xl:pl-25">
                    <img src="../../dist/img/homeschool.jpg" alt="Header Image" class="image rounded-md shadow-lg">
                </div>
            </div> <!-- header image -->
        </div> <!-- header hero -->
    </div>
</template>