<script setup>
import 
    { AcademicCapIcon, BuildingLibraryIcon, HomeIcon, UserIcon } 
from '@heroicons/vue/24/outline';
import { RouterLink } from 'vue-router';
</script>
<template>
    <div
        class="fixed flex flex-col top-10 left-0 w-14 border-r border-yellow-600 hover:w-64 md:w-64 h-full transition-all duration-300 z-10 sidebar">
        <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
            <ul class="flex flex-col py-4 space-y-1">
                <li class="px-5 hidden md:block">
                    <div class="bg-gray-50 text-center align-middle">
                        <div class="text-sm font-light tracking-wide uppercase">
                            HOMESCHOOLING
                        </div>
                    </div>
                </li>
                <li>
                    <RouterLink to="/"
                        :class="{'border-l-yellow-600': $route.path === '/'}"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-yellow-500 pr-6 m-3">
                        <span class="inline-flex justify-center items-center ml-4">
                            <HomeIcon class="w-5 h-5 text-lime-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Inicio</span>
                    </RouterLink>
                </li>
                <li>
                    <RouterLink to="/schools"
                        :class="{'border-l-yellow-600': $route.path === '/schools'}"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-yellow-500 pr-6 m-3">
                        <span class="inline-flex justify-center items-center ml-4">
                            <BuildingLibraryIcon class="w-5 h-5 text-lime-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Instituciones</span>
                    </RouterLink>
                </li>
                <li>
                    <RouterLink to="/students"
                        :class="{'border-l-yellow-600': $route.path === '/students'}"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-yellow-500 pr-6 m-3">
                        <span class="inline-flex justify-center items-center ml-4">
                            <AcademicCapIcon class="w-5 h-5 text-lime-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Profesores</span>
                    </RouterLink>
                </li>
                <li class="px-5 hidden md:block">
                    <div class="bg-gray-50 text-center align-middle">
                        <div class="text-sm font-light tracking-wide uppercase">
                            CONFIGURACIONES
                        </div>
                    </div>
                </li>
                <li>
                    <RouterLink to="/profile" 
                        :class="{'border-l-yellow-600': $route.path === '/profile'}"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-yellow-500 pr-6 m-3">
                        <span class="inline-flex justify-center items-center ml-4">
                            <UserIcon class="w-5 h-5 text-lime-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Perfil</span>
                    </RouterLink>
                </li>
            </ul>
            <p class="mb-14 px-5 py-3 hidden md:block text-center text-xs">Copyright @2023</p>
        </div>
    </div>
</template>