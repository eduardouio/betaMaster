<script setup>
    import { ref } from 'vue';
    import { UserGroupIcon, AcademicCapIcon, BuildingLibraryIcon, 
            HomeModernIcon, UserPlusIcon  } from '@heroicons/vue/24/outline';
    import { RouterLink } from 'vue-router';
    
    // props
    const props = defineProps(['itemSelected']);
    </script>
<template>
    <nav class="navbar bg-sky-100 text-xl drop-shadow-md bg-gradient-to-r from-gray-50 to-zinc-100">
        <!-- Menu movil -->
        <div class="navbar-start">
        <div class="dropdown">
            <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
                </svg>
            </div>
            <ul tabindex="0"
                class="menu menu-sm dropdown-content mt-3 z-[1] p-1 shadow bg-base-100 rounded-box w-screen mx-auto">
                <li>
                    <a to="/" :class="{ 'bg-slate-300 border-2': itemSelected === 'home' }">
                        <HomeModernIcon class="w-8 h-8" /> Inicio
                    </a>
                </li>
                <li :class="{ 'menu-item-active': itemSelected === 'colegios' }">
                    <a to="/colegios">
                        <BuildingLibraryIcon class="w-8 h-8" /> Colegios
                    </a>
                </li>
                <li :class="{ 'menu-item-active': itemSelected === 'maestros' }">
                    <a to="/maestros" class="menu-item">
                        <UserGroupIcon class="w-8 h-8" /> Maestros
                    </a>
                </li>
                <li>
                    <a class="text-md text-lime-800">Nuestra Oferta</a>
                    <ul class="p-2">
                        <li :class="{ 'menu-item-active': itemSelected === 'oferta-tecnica' }">
                            <a to="/bachillerato-tecnico">
                                <AcademicCapIcon class="w-8 h-8 text-blue-800" /> Bachillerato Técnico
                            </a>
                        </li>
                        <li :class="{ 'menu-item-active': itemSelected === 'oferta-general' }">
                            <a to="/bachillerato-general">
                                <AcademicCapIcon class="w-8 h-8 text-blue-800" /> Bachillerato General
                            </a>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
        <a class="text-md menu-item p-2">HomeScholing Ecuador</a>
    </div>
        <!-- /Menu movil -->
        <!-- Menu escritorio -->
        <div class="navbar-center hidden lg:flex gap-2">
                <ul class="menu menu-horizontal px-1 text-md hidden lg:flex gap-4">
                    <li class="menu-item" :class="{ 'menu-item-active': itemSelected === 'home' }">
                        <RouterLink to="/">
                            <HomeModernIcon class="w-6 h-6" />
                            Inicio
                        </RouterLink>
                    </li>
                    <li class="menu-item" :class="{ 'menu-item-active': itemSelected === 'colegios' }">
                        <a to="/colegios">
                            <BuildingLibraryIcon class="w-6 h-6" />
                            Colegios
                        </a>
                    </li>
                    <li class="menu-item" :class="{ 'menu-item-active': itemSelected === 'maestros' }">
                        <RouterLink to="/dashboard-teacher">
                            <UserGroupIcon class="w-6 h-6" />
                            Maestros
                        </RouterLink>
                    </li>
                    <li>
                        <details>
                            <summary class="menu-item">
                                <AcademicCapIcon class="w-6 h-6" />
                                Oferta
                            </summary>
                            <ul class="p-1 bg-base-100 rounded-t-none text-md">
                                <li :class="{ 'menu-item-active': itemSelected === 'oferta-tecnica' }">
                                    <a to="/bachillerato-tecnico" class="menu-item">
                                        <AcademicCapIcon class="w-6 h-6 text-blue-800" /> Bachillerato Técnico
                                    </a>
                                </li>
                                <li :class="{ 'menu-item-active': itemSelected === 'oferta-general' }">
                                    <a to="/bachillerato-general" class="menu-item">
                                        <AcademicCapIcon class="w-6 h-6 text-blue-800" /> Bachillerato General
                                    </a>
                                </li>
                            </ul>
                        </details>
                    </li>
                    <li :class="{ 'menu-item-active': itemSelected === 'oferta-tecnica' }">
                        <RouterLink to="/register" class="menu-item text-amber-800 text-xl">
                            <UserPlusIcon class="w-6 h-6 text-yellow-400" /> Regístrate
                        </RouterLink>
                    </li>
                </ul>
        </div>
        <!-- /Menu escritorio -->
    </nav>
</template>
