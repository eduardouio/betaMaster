<script setup>

import { reactive, ref, computed } from 'vue';
import  formRegistroEstudiante from '@/assets/img/formRegistroEstudiante.jpg';
import  formRegistroProfesor from '@/assets/img/formRegistroProfesor.jpg';
import  formRegistroColegio from '@/assets/img/formRegistroColegio.jpg';
import serverConfigData from '@/config.js';

const emits = defineEmits(['changeForm']);
const message = ref('');

const changeForm = function(){
    emits('changeForm');
}

const new_user = reactive({
    firstName: '',
    lastName: '',
    email: '',
    role: 'ESTUDIANTE',
    password: '',
    verify_password: ''
});

const passwordMatch = computed(()=>{
    if (new_user.password === '' && new_user.verify_password === ''){
        return true;
    }
    return new_user.password === new_user.verify_password;
});

const setPicture = computed(()=>{
    if (new_user.role === 'PROFESOR'){
        return formRegistroProfesor;
    }
    if (new_user.role === 'ESTUDIANTE'){
        return formRegistroEstudiante;
    }
    if (new_user.role === 'COLEGIO'){
        return formRegistroColegio;
    }
    return formRegistroEstudiante;
});

function registerUser(){
   const isValid = true;
    for (let key in new_user){
        if (new_user[key] === ''){
            alert('Todos los campos son requeridos');
            return false;
        }
    }
    if (isValid){sendData();}
}

// Enviamos lo datos al server
async function sendData(){
    try{
      let response = await fetch(serverConfigData.urls.registerUser, {
         method: 'POST',
         headers: serverConfigData.headers,
         body: JSON.stringify(new_user),
      });
      const data = await response.json();
      if (await response.status == 201){
        message.value = 'Registro exitoso, redireccionando...';
        setTimeout(()=>{
            window.location.href = serverConfigData.urls.login;
        }, 3000)
      }else{
         const error_message = Object.keys(data).map(key => data[key][0]);
         message.value = error_message.join(' ');
      }
      
}catch(error){
      alert('Error al enviar los datos al servidor, por favor intente de nuevo');
      console.dir(error);
   } 
}
</script>
<template>
    <div class="bg-white sm:bg-gray-200 min-h-screen w-screen">
       <div class="container bg-gray-200 mx-auto text-center">
          <span class="text-red-600 text-2xl" v-if="!passwordMatch">
          Las contraseñas no coinciden
          </span>
          <span>
            {{ message }}
          </span>
       </div>
       <div class="container mx-auto mt-4 bg-white p-10 rounded-xl border shadow-xl">
          <h5 class="p-1 text-center text-3xl font-bold m-5 md:m-10 text-gray-600">REGISTRO DE USUARIO</h5>
          <div class="flex justify-center">
             <!-- Row -->
             <div class="w-full flex flex-col md:flex-row rounded-l-lg xl:w-4/4 lg:w-12/12">
                <!-- Col -->
                <div class="w-full h-auto lg:block lg:w-5/12 rounded-l-lg sm:rounded-r-lg">
                   <img :src="setPicture" class="object-cover w-full h-full rounded-l-lg sm:rounded-r-lg border shadow-xl" alt="">
                </div>
                <!-- Col -->
                <div class="w-full lg:w-7/12 bg-white rounded-lg lg:rounded-l-none">
                   <div class="px-8 pt-6 pb-8 mb-4 rounded">
                      <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                         <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                            <label class="block mb-2 text-sm text-gray-700" for="firstName">
                            Nombres:
                            </label>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="font-medium text-2xl text-gray-600 absolute p-2.5 px-3 w-11">
                               <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                            </svg>
                            <input
                               class="py-2 pl-10 border border-gray-200 w-full" type="text" placeholder="Nombres" v-model="new_user.firstName" required/>
                         </div>
                         <div class="mb-4 flex-1 md:ml-2 md:mb-0">
                            <label class="block mb-2 text-sm text-gray-700" for="lastName">
                            Apellidos
                            </label>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="font-medium text-2xl text-gray-600 absolute p-2.5 px-3 w-11">
                               <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                            </svg>
                            <input
                               class="py-2 pl-10 border border-gray-200 w-full" type="text" placeholder="Apellidos" v-model="new_user.lastName" required/>
                         </div>
                      </div>
                      <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                         <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                            <label class="block mb-2 text-sm text-gray-700" for="email">
                            Email
                            </label>
                            <svg xmlns="http://www.w3.org/2000/svg" class="font-medium text-2xl text-gray-600 absolute p-2.5 px-3 w-11" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                            </svg>
                            <input
                               class="py-2 pl-10 border border-gray-200 w-full" type="email" placeholder="Email" 
                               v-model="new_user.email"/>
                         </div>
                         <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                            <label class="block mb-2 text-sm text-gray-700" for="email">
                            Soy
                            </label>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="font-medium text-2xl text-gray-600 absolute p-2.5 px-3 w-11">
                               <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 5.25 7.5 7.5 7.5-7.5m-15 6 7.5 7.5 7.5-7.5" />
                            </svg>
                            <select class="py-2 pl-10 border border-gray-200 w-full" v-model="new_user.role">
                               <option disabled selected>Quiero registrarme como...</option>
                               <option value="PROFESOR">Profesor</option>
                               <option value="ESTUDIANTE">Estudiante</option>
                               <option value="COLEGIO">Colegio</option>
                            </select>
                         </div>
                      </div>
                      <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                         <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                            <label class="block mb-2 text-sm text-gray-700" for="password">
                            Contraseña
                            </label>
                            <svg xmlns="http://www.w3.org/2000/svg" class="font-medium text-2xl text-gray-600 absolute p-2.5 px-3 w-11" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                            </svg>
                            <input
                               class="py-2 pl-10 border border-gray-200 w-full"
                               v-model="new_user.password"
                               type="password" placeholder="******************"
                               required />
                         </div>
                         <div class="md:ml-2 flex-1">
                            <label class="block mb-2 text-sm text-gray-700" for="c_password">
                            Confirmar
                            </label>
                            <svg xmlns="http://www.w3.org/2000/svg" class="font-medium text-2xl text-gray-600 absolute p-2.5 px-3 w-11" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                            </svg>
                            <input
                               class="py-2 pl-10 border border-gray-200 w-full"
                               v-model="new_user.verify_password"
                               type="password" placeholder="******************"
                               required />
                         </div>
                      </div>
                      <div class="mb-6 flex flex-col md:flex-row justify-between gap-2">
                         <button
                            @click="registerUser"
                            class="border border-indigo-500 hover:bg-indigo-500 hover:text-white duration-100 ease-in-out w-6/12 text-indigo-500 p-2 flex flex-row justify-center items-center gap-1"
                            type="button"
                            :disabled="!passwordMatch"  
                            >
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                            </svg>
                            Registrar Cuenta
                         </button>
                         <button
                            @click="changeForm"
                            class="border border-indigo-500 hover:bg-indigo-500 hover:text-white duration-100 ease-in-out w-6/12 text-indigo-500 p-2 flex flex-row justify-center items-center gap-1"
                            type="button">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
                            </svg>
                            Volver a Inicio
                         </button>
                      </div>
                   </div>
                </div>
             </div>
          </div>
       </div>
    </div>
 </template>
  