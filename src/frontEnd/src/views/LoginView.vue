<script setup>
import { RouterLink } from "vue-router";
import { ArrowLeftIcon } from "@heroicons/vue/24/outline";

</script>
<template>
<div class="min-h-screen flex flex-col justify-center sm:py-12">
  <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md card glass">
    <figure><img src="../assets/logo.jpeg" alt="car!"/></figure>
    <div class="border-blue-50">
      <div class="px-5 py-7">
        <label class="font-semibold text-sm text-gray-600 pb-1 block">Su Correo</label>
        <input type="text" class="my-input w-full" placeholder="direccion@dominio.com"/>
        <label class="font-semibold text-sm text-gray-600 pb-1 block">Su Contraseña</label>
        <input type="password" class="my-input w-full" placeholder="*****"/>
        <button type="button" class="btn btn-primary btn-block">
            <span class="text-white">Iniciar Sesión</span>
        </button>
      </div>
      <div class="py-5">
        <div class="grid grid-cols-2 gap-1">
          <div class="text-center sm:text-left whitespace-nowrap">
            <button class="transition duration-200 mx-5 px-5 py-4 cursor-pointer font-normal text-sm rounded-lg text-gray-500 hover:bg-gray-100 focus:outline-none focus:bg-gray-200 focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 ring-inset border border-cyan-700">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-4 h-4 inline-block align-text-top">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 11V7a4 4 0 118 0m-4 8v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2z" />
                </svg>
                <span class="inline-block ml-1">Recuperar Contraseña</span>
            </button>
            <RouterLink to="/" class="text-cyan-700">
                <ArrowLeftIcon class="w-4 h-4 inline-block align-text-top" />
                        Regresar
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>