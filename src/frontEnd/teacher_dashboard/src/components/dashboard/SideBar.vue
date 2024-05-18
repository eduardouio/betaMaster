3<script setup>
import 
    { AcademicCapIcon, BuildingLibraryIcon, HomeIcon, UserIcon } 
from '@heroicons/vue/24/outline';
import { RouterLink } from 'vue-router';
import { useStore } from 'vuex';



</script>
<template>
    <div
        class="fixed flex flex-col top-10 left-0 w-14 bg-gray-100 border-r border-slate-300 hover:w-64 md:w-64 h-full transition-all duration-300 z-10 sidebar">
        <div class="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
            <ul class="flex flex-col py-4 space-y-1">
                <li class="px-5 hidden md:block">
                    <div class="flex flex-row items-center h-8 border bg-gray-200 border-slate-300 rounded-xlqu">
                        <div class="text-md font-light tracking-wide uppercase pl-3">HOMESCHOOLING</div>
                    </div>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <HomeIcon class="w-5 h-5 text-sky-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Inicio</span>
                    </RouterLink>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher/schools"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <BuildingLibraryIcon class="w-5 h-5 text-sky-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Instituciones</span>
                    </RouterLink>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher/students"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <AcademicCapIcon class="w-5 h-5 text-sky-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Aspirantes</span>
                    </RouterLink>
                </li>
                <li class="px-5 hidden md:block">
                    <div class="flex flex-row items-center mt-5 h-8 border border-slate-300 bg-gray-200 rounded-xl">
                        <div class="text-md font-light tracking-wide uppercase pl-3">CONFIGURACIONES</div>
                    </div>
                </li>
                <li>
                    <RouterLink to="/dashboard-teacher/profile"
                        class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-base-100 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-blue-500 dark:hover:border-gray-800 pr-6">
                        <span class="inline-flex justify-center items-center ml-4">
                            <UserIcon class="w-5 h-5 text-sky-600" />
                        </span>
                        <span class="ml-2 text-sm tracking-wide truncate">Perfil</span>
                    </RouterLink>
                </li>
            </ul>
            <p class="mb-14 px-5 py-3 hidden md:block text-center text-xs">Copyright @2023</p>
        </div>
    </div>
</template>