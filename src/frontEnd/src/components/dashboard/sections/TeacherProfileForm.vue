<template>
  <div>
    <LoaderVue v-if="showLoader" />
    <div v-else class="p-1 bg-base flex items-center justify-center border rounded-md">
      <div class="max-w-screen-xl mx-auto">
        <div>
          <div class="grid grid-cols-1 lg:grid-cols-4">
            <div class="lg:col-span-2">
              <h2 class="font-semibold text-xl text-gray-700">Actualización de Perfil</h2>
            </div>
            <div class="lg:col-span-2 text-end">
              <span v-if="userData.user.is_aproved"
                class="badge rounded-md p-2 pl-3 pr-3 text-error hover:bg-error hover:text-white">
                <ExclamationTriangleIcon class="h-4 w-4 inline-block" />
                &nbsp;En Revisión
              </span>
              <span v-else class="badge rounded-md p-2 pl-3 pr-3 text-green-800 hover:text-white hover:bg-green-800">
                <CheckBadgeIcon class="h-4 w-4 inline-block" />
                &nbsp;Verificado
              </span>
            </div>
          </div>
          <div class="bg-white rounded shadow-lg p-4 px-4 md:p-5 mb-4">
            <div class="grid gap-y-1 text-sm grid-cols-1 lg:grid-cols-4 border-t border-zinc-300">
              <div class="text-gray-700 mt-5">
                <strong class="font-medium text-lg">Datos Personales</strong>
                <div class="card card-side flex items-center flex-col">
                  <figure>
                    <img
                      src="https://photoaid.com/en/tools/_next/static/images/before-25ed01ce5b208e9df51888c519ef7949.webp"
                      :alt="userData.user.first_name" class="w-2/3 h:auto" />
                  </figure>
                  <div class="flex flex-col xl:flex-row md:gap-2">
                    <small class="mt-3 btn btn-xs btn-primary text-white">Cambiar Imagen</small>
                    <small class="mt-3 btn btn-xs btn-primary text-white">Cambiar Clave</small>
                  </div>
                </div>
              </div>
              <div class="lg:col-span-3 mt-5">
                <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-6">
                  <div class="md:col-span-3">
                    <label for="first_name">
                      <strong class="text-red-500">*</strong>
                      Nombres
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Nombres" v-model="userData.user.first_name" />
                  </div>
                  <div class="md:col-span-3">
                    <label for="last_name">
                      <strong class="text-red-500">*</strong>
                      Apellidos
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Apellidos" v-model="userData.user.last_name" />
                  </div>
                  <div class="md:col-span-3">
                    <label for="dni_number">
                      <strong class="text-red-500">*</strong>
                      Identificación
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Identificación" v-model="userData.user.dni_number" />
                  </div>
                  <div class="md:col-span-3">
                    <label for="sex">
                      <strong class="text-red-500">*</strong>
                      Sexo
                    </label>
                    <select v-model="userData.user.sex" class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                    >
                      <option selected disabled>Seleccione...</option>
                      <option v-for="item in sexo" :key="item" :value="item" v-text="item"></option>
                    </select>
                  </div>
                  <div class="md:col-span-3">
                    <label for="country">
                      <strong class="text-red-500">*</strong>
                      Pais
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Apellidos" v-model="userData.user.country" readonly />
                  </div>
                  <div class="md:col-span-3">
                    <label for="email">
                      <strong class="text-red-500">*</strong>
                      Correo Electronico:
                      <small v-if="userData.user.is_confirmed_mail"
                        class="badge rounded-md p-2 pl-3 pr-3 text-error hover:bg-error hover:text-white">
                        <ExclamationTriangleIcon class="h-4 w-4 inline-block" />
                        &nbsp;Correo No Verificado
                      </small>
                      <small v-else
                        class="badge rounded-md p-2 pl-3 pr-3 text-green-800 hover:text-white hover:bg-green-800">
                        <CheckBadgeIcon class="h-4 w-4 inline-block" />
                        &nbsp;Correo Verificado
                      </small>
                    </label>
                    <input type="email" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="nombre@dominio.com" v-model="userData.user.email" readonly />
                  </div>
                  <div v class="md:col-span-3">
                    <label for="date_of_birth">
                      <strong class="text-red-500">*</strong>
                      Fecha de Nacimiento
                    </label>
                    <input type="date" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Nacimiento" v-model="userData.user.date_of_birth" />
                  </div>
                  <div class="md:col-span-3">
                    <label for="geolocation">
                      <strong class="text-red-500">*</strong>
                      Geolocalización
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Ubicación" v-model="userData.user.geolocation" />
                  </div>
                  <div class="md:col-span-4">
                    <label for="address">
                      <strong class="text-red-500">*</strong>
                      Dirección:
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Dirección" v-model="userData.user.address" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="country">
                      <strong class="text-red-500">*</strong>
                      Pais
                    </label>
                    <input type="text" maxlength="13"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11" placeholder="Su Pais"
                      v-model="userData.user.country" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="state">
                      <strong class="text-red-500">*</strong>
                      Provincia
                    </label>
                    <div class="h-10 bg-gray-50 rounded items-center">
                      <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                        v-model="userData.user.state">
                        <option v-for="item in states" v-text="item" :value="item" :key="item">
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="md:col-span-2">
                    <label for="state">
                      <strong class="text-red-500">*</strong>
                      Cantón
                    </label>
                    <div class="h-10 bg-gray-50 rounded items-center">
                      <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                        v-model="userData.user.city">
                        <option v-for="item in cities" :key="item" :value="item" v-text="item">
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="md:col-span-2">
                    <label for="parroquia">
                      <strong class="text-red-500">*</strong>
                      Parroquia
                    </label>
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                      v-model="userData.user.parroquia">
                      <option v-for="item in parroquias" :key="item" :value="item" v-text="item">
                      </option>
                    </select>
                  </div>
                  <div class="md:col-span-2">
                    <label for="phone">
                      <strong class="text-red-500">*</strong>
                      Celular
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Celular" v-model="userData.user.phone" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="phone_2">Tel Fijo</label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Teléfono" v-model="userData.user.phone_2" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="civil_status"><strong class="text-red-500">*</strong> Estado Civil</label>
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                      v-model="userData.user.civil_status">
                      <option disabled> Seleccione...</option>
                      <option value="SOLTERO"> SOLTERO</option>
                      <option value="CASADO"> CASADO</option>
                      <option value="DIVORCIADO"> DIVORCIADO</option>
                      <option value="VIUDO"> VIUDO</option>
                      <option value="SEPARADO"> SEPARADO</option>
                      <option value="OTRO"> OTRO</option>
                    </select>
                  </div>
                  <div class="md:col-span-3 md:mt-4 md:border md:rounded-xl">
                    <label class="label cursor-pointer">
                      <span class="label-text">¿Hago HomeSchooling?</span>
                      <input 
                        type="checkbox"
                        class="checkbox"
                        v-model="userData.user.is_homescholing"
                        />
                    </label>
                  </div>
                  <div class="md:col-span-3 md:mt-4 md:border md:rounded-xl">
                    <label class="label cursor-pointer">
                      <span class="label-text">¿Puedo Reemplazar?</span>
                      <input 
                        type="checkbox" 
                        class="checkbox"
                        v-model="userData.user.is_replacement"
                        />
                    </label>
                  </div>
                </div>
                <div class="lg:col-span-3 mt-5 p-3">
                  <span class="text-info uppercase">Cuentanos un poco de Ti</span>
                  <hr class="m-3" />
                  <TextEditor 
                    v-if="showPresentation"
                    class="h-100"
                    :text="userData.user.presentation"
                    @handleTextEditor="handleTextEditor($event)"
                    >
                  </TextEditor>
                </div>
                <div class="lg:col-span-3 mt-5 p-3">
                  <span class="text-info uppercase">Redes Sociales</span>
                  <hr class="m-3" />
                  <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-4">
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="facebook" />
                        <label for="url_facebook">Facebook</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="Su Facebook" v-model="userData.user.url_facebook" />
                    </div>
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="linkedin" />
                        <label for="url_linkedin">Linkedind</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="Su Facebook" v-model="userData.user.url_linkedin" />
                    </div>
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="instagram" />
                        <label for="url_instagram">Instagram</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="Su Facebook" v-model="userData.user.url_instagram" />
                    </div>
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="twitter" />
                        <label for="url_twiter">Twitter</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="Su Facebook" v-model="userData.user.url_twiter" />
                    </div>
                  </div>
                </div>
                <div class="lg:col-span-3 mt-5 bg-gray-100 p-3">
                  <span class="text-info uppercase">Capacidades Especiales</span>
                  <hr class="m-3" />
                  <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-6">
                    <div class="md:col-span-3">
                      <label for="have_disability">Tiene alguna discapacidad?</label>
                      <br>
                      <input type="checkbox" class="checkbox" v-model="userData.user.have_disability" />
                      <span class="ml-3 text-success" v-if="userData.user.have_disability">SI, Especifique</span>
                      <span class="ml-3 text-info" v-else>Ninguna</span>
                    </div>
                    <div class="md:col-span-3" v-if="userData.user.have_disability">
                      <label for="type_disability">Tipo de discapacidad</label>
                      <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                        v-model="userData.user.type_disability">
                        <option select>Seleccione...</option>
                        <option value="MOTRIZ">MOTRIZ</option>
                        <option value="AUDITIVA">AUDITIVA</option>
                        <option value="VISUAL">VISUAL</option>
                        <option value="INTELECTUAL">INTELECTUAL</option>
                        <option value="OTRA">OTRA</option>
                      </select>
                    </div>
                    <div class="md:col-span-3" v-if="userData.user.have_disability">
                      <label for="disability_persent">Porcentaje</label>
                      <input type="number" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="Su Teléfono" v-model="userData.user.disability_persent" />
                    </div>
                    <div class="md:col-span-3" v-if="userData.user.have_disability">
                      <label for="card_conadis">Nro de Carnet</label>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        placeholder="Su Teléfono" v-model="userData.user.card_conadis" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="grid gap-y-1 text-sm grid-cols-1 lg:grid-cols-4 pt-10 border-t border-zinc-300 mt-8">
              <div class="text-gray-700 ">
                <strong class="font-medium text-lg">Experiencia Profesional</strong>
                <div class="card card-side bg-base-100">
                </div>
              </div>
              <div class="lg:col-span-3">
                <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-6">
                  <div class="md:col-span-3">
                    <label for="level_education">Nivel de Educación</label>
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                      v-model="userData.user.level_education">
                      <option selected>seleccione....</option>
                      <option value="PRIMARIA">PRIMARIA</option>
                      <option value="SECUNDARIA">SECUNDARIA</option>
                      <option value="SUPERIOR">SUPERIOR</option>
                      <option value="POSTGRADO">POSTGRADO</option>
                      <option value="MASTER">MASTER</option>
                      <option value="DOCTOR">DOCTOR</option>
                      <option value="OTRO">OTRO</option>
                    </select>
                  </div>
                  <div class="md:col-span-3">
                    <label for="profesion">Profesión</label>
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-8"
                      v-model="userData.user.profesion">
                      <option selected>seleccione....</option>
                      <option value="PROFESOR">PROFESOR</option>
                      <option value="LICIENCIADO">LICIENCIADO</option>
                      <option value="TÉCNICO">TÉCNICO</option>
                      <option value="TECNÓLOGO">TECNÓLOGO</option>
                      <option value="INGENIERO">INGENIERO</option>
                      <option value="MEDICO">MEDICO</option>
                      <option value="ABOGADO">ABOGADO</option>
                      <option value="ECONOMISTA">ECONOMISTA</option>
                      <option value="ADMINISTRADOR">ADMINISTRADOR</option>
                      <option value="OTRO">OTRO</option>
                    </select>
                  </div>
                  <div class="md:col-span-6">
                    <label for="full_name">Hoja de Vida PDF</label>
                    <input type="file" class="input input-sm input-bordered input-secondary focus:input-primary w-full"
                      placeholder="Sus Nombres" />
                  </div>
                  <div class="md:col-span-6 pt-2 bg-gray-50 p-4 border rounded-md">
                    <label for="profesion">Disiplinas</label>
                    <ul class="flex flex-col md:flex-row gap-4 md:pt-4">
                      <li 
                        v-for="item in JSON.parse(userData.user.disipline).disiplinas"
                        :key="item"
                        class="badge badge-primary badge-outline"
                        > {{ item }}
                      </li>
                    </ul>
                    <hr class="m-3"/>
                    <ul class="flex flex-col md:flex-row gap-4 md:pt-4">
                      <li>QUIMICA</li>
                      <li>QUIMICA</li>  
                      <li>QUIMICA</li>
                    </ul>
                  </div>

                  <div class="lg:col-span-6 mt-5 bg-gray-100 p-3">
                      espacio  para las referencias
                  </div>
                  <div class="md:col-span-6">
                  </div>
                </div>
              </div>
              <div class="md:col-span-6 text-right py-5">
                <div class="inline-flex items-end">
                  <button @click="updateProfile" class="btn btn-primary text-white btn-sm">
                    <FolderArrowDownIcon class="w-5 h-5 text-white"/>
                    Actualizar Información
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Toast
      v-if="toastMessage.showToast" 
      :typeToast="toastMessage.typeToast"
      :statusResponse="statusResponse"
    />
  </div>
</template>
<script setup>
import { useStore } from 'vuex';
import { computed, onMounted, ref, reactive } from 'vue';
import {
  ExclamationTriangleIcon, CheckBadgeIcon, FolderArrowDownIcon,
  CheckIcon, XCircleIcon, XMarkIcon, PencilSquareIcon
}
  from '@heroicons/vue/24/outline';

import serverInteractions from '@/server-interactions.js';
import serverConfigData from '@/config.js';

import provincias from '@/assets/provincias.json';
import LoaderVue from '@/components/generics/Loader.vue';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import TextEditor from '@/components/generics/TextEditor.vue';
import Toast  from '@/components/dashboard/Toast.vue';


const toastMessage = reactive({
  showToast: false,
  message: '',
  typeToast: 'error',
});

const store = useStore();
const showLoader = ref(true);
const showError = ref(false);
let states = ref([]);
let cities = ref([]);
let parroquias = ref([]);
let userData = ref(null);
const password = ref({
  password: '',
  password_2: '',

});
let userPresentation = ref('');
let showPresentation = ref(true);
const sexo = ref(['FEMENINO', 'MASCULINO', 'OTRO']);
const statusResponse = computed(() => store.state.statusResponse);

onMounted(async () => {
  showLoader.value = true;
  userData = await store.state.userData;

  if (!userData) {
    getUserData();
  }

  states = Object.values(provincias).map(item => item.provincia);
  cities = Object.values(
    Object.values(provincias).filter(
      item => item.provincia === userData.user.state)[0].cantones
  ).map(item => item.canton);
  parroquias = Object.values(
    Object.values(
      Object.values(provincias).filter(
        item => item.provincia === userData.user.state)[0].cantones
    ).map(item => item).filter(
      item => item.canton === userData.user.city)[0].parroquias);
  if (userData) {
    showLoader.value = false;
  }
});


// recuperamos los datos del usuario y lo colocamos en el store
async function getUserData() {
  showLoader.value = false;
  let url = serverConfigData.urls.getUser.replace(
    '{idUser}', serverConfigData.idUser
  );
  let response = await serverInteractions.getData(url);
  if (response.status.is_success) {
    store.commit('setUserData', response.response);
    store.commit('setStatusResponse', response.status);
    userData = store.state.userData;
    showLoader.value = false;
  } else {
    console.log('Error al cargar los datos del dashboard');
  }

  if (statusResponse.value.is_success) {
    showToast('Datos actualizados correctamente', 'success');
  } else {
    showToast('Error al actualizar los datos', 'error');
  }
} 

async function updateProfile() {

  showError.value = true;
  if (userPresentation){
    showPresentation.value = false;
    userData.user.presentation = userPresentation;
  }
  await store.dispatch('updateProfile', userData);
  userData = await store.state.userData;
  setTimeout(() => {
    showPresentation.value = true;
  }, 200);

  if (statusResponse.value.is_success) {
    showToast('success');
  } else {
      showToast('error');
  }

}

const showToast = (typeToast) => {
  toastMessage.showToast = true;
  toastMessage.typeToast = typeToast;
  setTimeout(() => {
    toastMessage.showToast = false;
  }, 4000);
}

const handleTextEditor = (event) => {
  userPresentation = event;
}

</script>