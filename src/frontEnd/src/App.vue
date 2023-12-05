<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { UserGroupIcon, AcademicCapIcon, BuildingLibraryIcon, HomeModernIcon, UserPlusIcon  } from '@heroicons/vue/24/outline'

</script>
<template>
  <div>
    <nav class="navbar bg-sky-100 text-md drop-shadow-md bg-gradient-to-r from-teal-200 to-green-200">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
          </svg>
          
        </div>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-1 shadow bg-base-100 rounded-box w-screen mx-auto">
          <li><a> <HomeModernIcon class="w-8 h-8"/> Inicio</a></li>
          <li><a> <BuildingLibraryIcon class="w-8 h-8"/> Colegios</a></li>
          <li><a> <UserGroupIcon class="w-8 h-8"/> Maestros</a></li>
          <li>
            <a class="text-md text-lime-800">Nuestra Oferta</a>
            <ul class="p-2">
              <li><a href=""><AcademicCapIcon class="w-8 h-8 text-blue-800"/> Bachillerato Técnico</a></li>
              <li><a href=""><AcademicCapIcon class="w-8 h-8 text-blue-800"/> Bachillerato General</a></li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="navbar-start">
        <a class="text-md">HomeScholing Ecuador</a>        
      </div>
      <div class="navbar-end  gap-1">
        <ul class="menu menu-horizontal px-1 text-md hidden lg:flex">
          <li><a class="hover:bg-base-100 hover:text-blue-800">
            <HomeModernIcon class="w-6 h-6"/>
            Inicio
          </a></li>
          <li><a class="hover:bg-base-100 hover:text-blue-800 ">
            <BuildingLibraryIcon class="w-6 h-6"/>
 Colegios
</a></li>
          <li><a class="hover:bg-base-100 hover:text-blue-800">
            <UserGroupIcon class="w-6 h-6"/>
          Maestros
          </a></li>
          <li>
            <details>
              <summary class="hover:bg-base-100 hover:text-blue-800">
                <AcademicCapIcon class="w-6 h-6"/>
                Nuestra Oferta
              </summary>
              <ul class="p-1 bg-base-100 rounded-t-none text-md">
                <li><a href=""><AcademicCapIcon class="w-6 h-6 text-blue-800"/> Bachillerato Técnico</a></li>
                <li><a href=""><AcademicCapIcon class="w-6 h-6 text-blue-800"/> Bachillerato General</a></li>
              </ul>
            </details>
          </li>
        </ul>
        <div class="dropdown dropdown-end">
          <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar text-blue-400">
            <div class="w-8 rounded-full text-blue-600 justify-content-center">
              <UserPlusIcon class="w-6 h-6"/>
            </div>
          </div>
          <ul tabindex="0" class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
            <li p-4 m-3>
              <div class="card bg-yellow-300 shadow-xl">
                <div class="card-body">
                  <h2 class="card-title text-md text-black">¡Únete!</h2>
                  <p class="text-black">Ven, y formar parte de la mejor comunidad de estudios en casa del Ecuador</p>
                  <div class="card-actions justify-center">
                    <button class="btn btn-primary">Registrarme</button>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <header>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </header>
    <RouterView />
  </div></template>
