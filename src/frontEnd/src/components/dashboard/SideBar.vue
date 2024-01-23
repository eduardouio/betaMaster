<script setup>
import 
    { AcademicCapIcon, BuildingLibraryIcon, HomeIcon, UserIcon } 
from '@heroicons/vue/24/outline';
import { RouterLink } from 'vue-router';
</script>
<template>
    <div
        class="fixed flex flex-col top-14 left-0 w-14 hover:w-64 md:w-64 bg-gradient-to-t from-gray-700 to-gray-800 dark:bg-gray-900 h-full text-white transition-all duration-300 border-none z-10 sidebar">
        <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
            <ul class="flex flex-col py-4 space-y-1">
                <li class="px-5 hidden md:block">
                    <div class="flex flex-row items-center h-8">
                        <div class="text-md font-light tracking-wide text-white uppercase"></div>
                    </div>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-cyan-600 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <HomeIcon class="w-5 h-5" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Inicio</span>
                    </RouterLink>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher/schools"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-cyan-600 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <BuildingLibraryIcon class="w-5 h-5" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Instituciones</span>
                        <span
                            class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-red-500 bg-red-50 rounded-full">2</span>
                    </RouterLink>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher/students"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-cyan-600 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <AcademicCapIcon class="w-5 h-5" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Estudiantes</span>
                        <span
                            class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-red-500 bg-red-50 rounded-full">2</span>
                    </RouterLink>
                </li>
                <li class="px-5 hidden md:block">
                    <div class="flex flex-row items-center mt-5 h-8">
                        <div class="text-md font-light tracking-wide text-white uppercase">CONFIGURACIONES</div>
                    </div>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher/profile"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-cyan-600 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <UserIcon class="w-5 h-5" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Perfil</span>
                    </RouterLink>
                </li>
            </ul>
            <p class="mb-14 px-5 py-3 hidden md:block text-center text-xs">Copyright @2023</p>
        </div>
    </div>
</template>