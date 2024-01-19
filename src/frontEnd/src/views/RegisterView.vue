<script setup>
import { onMounted } from 'vue';
import NavBar from '../components/NavBar.vue';
import { ref, shallowReactive, TransitionGroup } from 'vue';
import { UserPlusIcon } from '@heroicons/vue/24/outline';
import serverConfigData from '../config.js';
import WarningMessage from '../components/generics/WarningMessage.vue';
import Loader from '../components/generics/Loader.vue';

const new_user = ref({
    firstName: 'Eduardo',
    lastName: 'Villota',
    email: 'eduard@gmsiom.com',
    role: 'teacher',
    password: '1234',
    verify_password: '1234'
});

const message = ref('');
const type_message = ref('error');
const loader = ref(false);

function registerUser(){
    message.value = '';
    console.log(new_user.value.password);
    // verificamos las contraseñas
    if (new_user.value.password != new_user.value.verify_password){
        message.value = 'Las contraseñas no coinciden';
        return false;
    }    

    // verificamos todos los demas datos
    const inputs = {
        firstName: 'Nombres',
        lastName: 'Apellidos',
        email: 'Email',
        role: 'Rol',
        password: 'Contraseña',
        verify_password: 'Confirmar Contraseña'
    }

    for (let key in new_user.value){
        if (new_user.value[key] == ''){
            message.value = 'El campo ' + inputs[key] + ' es obligatorio';
            type_message.value = 'warning';
            return false;
        }
    }
    loader.value = true;
    sendData();
    return true;
}

// Enviamos lo datos al server
async function sendData(){
    message.value = '';
    let response = await fetch(serverConfigData.urls.registerUser, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(new_user.value),
    });
    const data = await response.json();
    loader.value = false;
    if (response.status == 201){
        message.value = 'Registro exitoso, redireccionando...';
        type_message.value='success';
        setTimeout(()=>{
            window.location.href = serverConfigData.urls.login;
        }, 2000);
    }

    if (response.status === 403){
        message.value = `Error en el registro ${data.detail}`;
        type_message.value = 'error';
    }

    if (response.status === 400){
        let msg_reponse = data[Object.keys(data)[0]];
        message.value = `Error en el registro ${response.statusText} ${msg_reponse}`;
        type_message.value = 'error';
    }
}



</script>

<template>
    <div>
      <NavBar :itemSelected="'register'"/>
      <div class="">
        <!-- Container -->
        <div class="container mx-auto mt-4">
            <WarningMessage v-if="message" :message="message" :type_message="type_message"/>
            <h5 class="p-1 text-center text-cyan-900 bg-gradient-to-r from-gray-100  to-slate-100 border">REGISTRO DE USUARIO</h5>
            <div class="flex justify-center px-6 my-6">
                <!-- Row -->
                <div class="w-full flex flex-col md:flex-row rounded-l-lg xl:w-4/4 lg:w-12/12">
                    <!-- Col -->
                    <div class="w-full h-auto bg-gray-400 lg:block lg:w-5/12 rounded-l-lg sm:rounded-r-lg">
                        <img src="../assets/form-registro.jpg" class="object-cover w-full h-full rounded-l-lg sm:rounded-r-lg" alt="">
                    </div>
                    <!-- Col -->
                    <div class="w-full lg:w-7/12 bg-white rounded-lg lg:rounded-l-none">
                        <div class="px-8 pt-6 pb-8 mb-4 rounded">
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="firstName">
                                        Nombres:
                                    </label>
                                    <input
                                        class="my-input w-full max-w-xs x-input" type="text" placeholder="Nombres" v-model="new_user.firstName"/>
                                </div>
                                <div class="mb-4 flex-1 md:ml-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="lastName">
                                        Apellidos
                                    </label>
                                    <input
                                        class="my-input w-full max-w-xs x-input" type="text" placeholder="Nombres" v-model="new_user.lastName"/>
                                </div>
                            </div>
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="email">
                                    Email
                                </label>
                                <input
                                    class="my-input w-full max-w-xs x-input" type="email" placeholder="Email" 
                                    v-model="new_user.email"/>
                                </div>
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="email">
                                    Soy
                                </label>
                                <select class="select w-full max-w-xs selected px-3  mb-3 x-input" name="new_user.role">
                                <option disabled selected>Quiero registrarme como...</option>
                                    <option value="teacher">Profesor</option>
                                    <option value="student">Estudiante</option>
                                    <option value="school">Colegio</option>
                                </select>
                            </div>                                
                            </div>                                
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="password">
                                        Contraseña
                                    </label>
                                    <input
                                        class="w-full px-3 py-2 mb-3 x-input"
                                        v-model="new_user.password"
                                        type="password" placeholder="******************" />
                                </div>
                                <div class="md:ml-2 flex-1">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="c_password">
                                        Confirmar
                                    </label>
                                    <input
                                        class="w-full px-3 py-2 mb-3 x-input"
                                        v-model="new_user.verify_password"
                                        type="password" placeholder="******************" />
                                </div>
                            </div>
                            <div class="mb-6 text-center">
                                <button
                                    v-if="!loader"
                                    @click="registerUser"
                                    class="btn btn-primary text-white"
                                    type="button">
                                    <UserPlusIcon class="h-6 w-6 mr-2"/>
                                    Registrar Cuenta
                                </button>
                                <Loader v-else/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>
  