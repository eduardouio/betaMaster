<script setup>
    import { UserCircleIcon } from '@heroicons/vue/24/outline';
    import { useStore } from 'vuex';
    const store = useStore();
    const profile = store.getters.getProfile;
</script>
<template>
    <!-- Header -->
    <div class="fixed w-full flex items-center justify-between h-10 z-10">
        <div class="flex items-center justify-start md:justify-center pl-3 w-14 md:w-64 h-10 bg-yellow-500 ">
            <UserCircleIcon class="w-5 h-5 md:mr-10" />
            <span class="hidden md:block uppercase text-base-100"> {{ profile.first_name }} {{ profile.last_name
                }}</span>
        </div>
        <div class="flex justify-between items-center h-10 bg-yellow-500  header-right border-b border-yellow-600">
            <div class="rounded flex items-center w-full max-w-xl mr-4 p-2 uppercase">

            </div>
            <ul class="flex items-center">
                <li>
                    <a href="#" class="flex items-center mr-4 hover:text-blue-800">
                        <span class="inline-flex mr-1">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1">
                                </path>
                            </svg>
                        </span>
                        Salir
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <!-- ./Header -->
</template>