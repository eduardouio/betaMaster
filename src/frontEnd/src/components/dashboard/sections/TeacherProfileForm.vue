<script setup>
import { useStore } from 'vuex';
import { computed, ref, reactive, onMounted } from 'vue';
import {
  ExclamationTriangleIcon, CheckBadgeIcon, FolderArrowDownIcon,
  CheckIcon, XCircleIcon, XMarkIcon, PencilSquareIcon, KeyIcon, PhotoIcon,
  MapPinIcon
}
  from '@heroicons/vue/24/outline';

import serverInteractions from '@/server-interactions.js';
import serverConfigData from '@/config.js';

import provincias from '@/assets/provincias.json';
import LoaderVue from '@/components/generics/Loader.vue';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import TextEditor from '@/components/generics/TextEditor.vue';
import Toast from '@/components/dashboard/Toast.vue';
import Skills from '@/components/dashboard/Skills.vue';
import ModalPasswordForm from '@/components/dashboard/ModalPasswordForm.vue';
import ModalPictureForm from '@/components/dashboard/ModalPictureForm.vue';
import PersonalReferences from '@/components/dashboard/sections/PersonalReferences.vue';
import MapSelector from '@/components/dashboard/MapSelector.vue';
import ProfilePicMen from '@/assets/profile-pic-men.png';
import ProfilePicWomen from '@/assets/profile-pic-woman.png';

onMounted(() => {
  loadStates();
});

const showMapSelector = ref(false);
const toastMessage = ref({
  showToast: false,
  typeToast: 'error',
});
const store = useStore();
const showError = ref(false);
let states = ref([]);
let cities = ref([]);
let parroquias = ref([]);
let showPresentation = ref(true);
let showPasswordModal = ref(false);
let showPictureModal = ref(false);
const sexo = ref(['FEMENINO', 'MASCULINO', 'OTRO']);
let userPresentation = '';

let userData = store.getters.getProfile;
const statusResponse = computed(() => store.getters.getStatusResponse);
const showLoader = computed(() => store.getters.getIsLoading);
const profilePic = computed(() => {
    if (store.getters.getPicture) {
        return store.getters.getPicture
    }
    if (userData.sex === 'FEMENINO') {
        return ProfilePicWomen;
    }
    return ProfilePicMen;
});

const urlCV = computed(() => store.getters.getCV);

const loadStates = function (state=null, city=null, parroquia=null) {
  states.value = Object.values(provincias).map(item => item.provincia);
  if (!state){
    cities.value = Object.values(
    Object.values(provincias).filter(
      item => item.provincia === userData.state)[0].cantones
    ).map(item => item.canton);
  }else{
    cities.value = Object.values(
    Object.values(provincias).filter(
      item => item.provincia === state)[0].cantones
    ).map(item => item.canton);

  }
  
  parroquias.value = Object.values(
    Object.values(
      Object.values(provincias).filter(
        item => item.provincia === userData.state)[0].cantones
    ).map(item => item).filter(
      item => item.canton === userData.city)[0].parroquias);
};

async function updateProfile() {
  toastMessage.value.showToast = false;
  if (userPresentation) {
    showPresentation.value = false;
    userData.presentation = userPresentation;
  }
  const response = await store.dispatch('updateProfile', userData);
  store.commit('setStatusResponse', await response);
  if (await response.status.is_success) {
    showToast('success');
  } else {
    showToast('error');
  }
}

const changePicture = async function(file){
  const formData = new FormData();
  formData.append('file', file);
  const response = await store.dispatch('updateProfileImage', formData);
  store.commit('setStatusResponse', await response);
  
  if (await response.status.is_success) {
    showToast('success');
  }else {
    showToast('error');
  }
}

const changePassword = async function(event){
  showLoader.value = true;

  const response = await store.dispatch(
    'updateProfilePasswod', {password: event.password}
  );
  store.commit('setStatusResponse', await response);
  if (await response) {
    showToast('success');
  } else {
    showToast('error');
  }
  showLoader.value = false;
};

const showToast = (typeToast) => {
  toastMessage.value.showToast = true;
  toastMessage.value.typeToast = typeToast;
  setTimeout(() => {
    toastMessage.value.showToast = false;
  }, 4000);
}

const handleTextEditor = (event) => {
  userPresentation = event;
  showMapSelector.value = false;
}

const handleUpdateSkills = (event) => {
  userData.disipline = event;
}

const handelCoordinates = (event) => {
  userData.geolocation = event;
} 

const handelModalMap = function(){
  console.log('cerrar modal');
  showMapSelector.value = false;
}

const handleFileUpload = async (event) => {
  const file = event.target.files[0];
  if (!file) {
    return;
  }

  showError.value = true;
  const formData = new FormData();
  formData.append('file', file);

  let url = serverConfigData.urls.uploadCVFile.replace(
    '{idUser}', serverConfigData.idUser
  ) + file.name;

  const response = await serverInteractions.postFile(url, formData);
  store.commit('setStatusResponse', response);

  if (response.status.is_success) {
    userData.cv = serverConfigData.baseUrl + response.response.url;
    store.commit('setUserData', JSON.parse(JSON.stringify(userData)));
  }

  if (statusResponse.value.is_success) {
    showToast('success');
  } else {
    showToast('error');
  }
};

const handelModalPassword = function(){
  showPasswordModal.value = !showPasswordModal.value;
};

const handelModalPicture = function(){
  showPictureModal.value = !showPictureModal.value;
};
</script>
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
              <span v-if="userData.is_aproved"
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
                      :src="profilePic"
                      :alt="userData.first_name" class="w-2/3 h:auto" />
                  </figure>
                  <div class="flex flex-col 2xl:flex-row md:gap-2">
                    <a class="mt-3 btn btn-xs btn-primary text-white"
                      @click="handelModalPicture"
                    >
                      <PhotoIcon class="h-4 w-4 inline-block" />
                      Cambiar Imagen
                    </a>
                    <a class="mt-3 btn btn-xs btn-primary text-white"
                      @click="handelModalPassword">
                      <KeyIcon class="h-4 w-4 inline-block" />
                      Cambiar Clave
                    </a>
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
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Sus Nombres" v-model="userData.first_name" />
                  </div>
                  <div class="md:col-span-3">
                    <label for="last_name">
                      <strong class="text-red-500">*</strong>
                      Apellidos
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Sus Apellidos" v-model="userData.last_name" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="dni_number">
                      <strong class="text-red-500">*</strong>
                      Identificación
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Su Identificación" v-model="userData.dni_number" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="sex">
                      <strong class="text-red-500">*</strong>
                      Sexo
                    </label>
                    <select v-model="userData.sex" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                    >
                      <option selected disabled>Seleccione...</option>
                      <option v-for="item in sexo" :key="item" :value="item">{{ item }}</option>
                    </select>
                  </div>
                  <div class="md:col-span-2">
                    <label for="civil_status"><strong class="text-red-500">*</strong> Estado Civil</label>
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      v-model="userData.civil_status">
                      <option disabled> Seleccione...</option>
                      <option value="SOLTERO"> SOLTERO</option>
                      <option value="CASADO"> CASADO</option>
                      <option value="DIVORCIADO"> DIVORCIADO</option>
                      <option value="VIUDO"> VIUDO</option>
                      <option value="SEPARADO"> SEPARADO</option>
                      <option value="OTRO"> OTRO</option>
                    </select>
                  </div>
                  <div class="md:col-span-2">
                    <label for="email">
                      <strong class="text-red-500">*</strong>
                      Correo Electronico:
                      <small v-if="userData.is_confirmed_mail"
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
                    <input type="email" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="nombre@dominio.com" v-model="userData.email" readonly />
                  </div>
                  <div v class="md:col-span-2">
                    <label for="date_of_birth">
                      <strong class="text-red-500">*</strong>
                      Fecha de Nacimiento
                    </label>
                    <input type="date" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Nacimiento" v-model="userData.date_of_birth" />
                  </div>
                
                  <div class="md:col-span-2">
                    <label for="phone">
                      <strong class="text-red-500">*</strong>
                      Celular
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Su Celular" v-model="userData.phone" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="phone_2">Tel Fijo</label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Su Teléfono" v-model="userData.phone_2" />
                  </div>
      
                  <div class="md:col-span-4">
                    <label for="address">
                      <strong class="text-red-500">*</strong>
                      Dirección:
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Su Dirección" v-model="userData.address" />
                  </div>
                  <div class="md:col-span-2">
                    <label for="state">
                      <strong class="text-red-500">*</strong>
                      Provincia
                    </label>
                    <div class="h-10 bg-gray-50 rounded items-center">
                      <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        v-model="userData.state" @change="loadStates(state=userData.state)">
                        <option v-for="item in states" :value="item" :key="item">
                          {{ item }}
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
                      <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        v-model="userData.city" @change="loadStates(state=userData.state, city=userData.city)">
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
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      v-model="userData.parroquia">
                      <option v-for="item in parroquias" :key="item" :value="item" v-text="item">
                      </option>
                    </select>
                  </div>
                  <div class="md:col-span-2">
                    <label for="geolocation">
                      <strong class="text-red-500">*</strong>
                      Geolocalización
                    </label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      placeholder="Ubicación" v-model="userData.geolocation"  readonly/>
                  </div>
                  <div class="md:col-span-2">
                    <span @click="showMapSelector=true" class="btn btn-sm bg-slate-500 text-white">
                      <MapPinIcon class="w-5 h-5"/>
                      Obtener Ubicación
                    </span>
                  </div>
                  <div class="md:col-span-3 md:mt-4 md:border md:rounded-xl">
                    <label class="label cursor-pointer">
                      <span class="label-text">¿Hago HomeSchooling?</span>
                      <input 
                        type="checkbox"
                        class="checkbox"
                        v-model="userData.is_homescholing"
                        />
                    </label>
                  </div>
                  <div class="md:col-span-3 md:mt-4 md:border md:rounded-xl">
                    <label class="label cursor-pointer">
                      <span class="label-text">¿Puedo Reemplazar?</span>
                      <input 
                        type="checkbox" 
                        class="checkbox"
                        v-model="userData.is_replacement"
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
                    :text="userData.presentation"
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
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        placeholder="Su Facebook" v-model="userData.url_facebook" />
                    </div>
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="linkedin" />
                        <label for="url_linkedin">Linkedind</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        placeholder="Su Facebook" v-model="userData.url_linkedin" />
                    </div>
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="instagram" />
                        <label for="url_instagram">Instagram</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        placeholder="Su Facebook" v-model="userData.url_instagram" />
                    </div>
                    <div class="md:col-span-2">
                      <div class="flex gap-4">
                        <SocialIcon url="#" icon="twitter" />
                        <label for="url_twiter">Twitter</label>
                      </div>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        placeholder="Su Facebook" v-model="userData.url_twiter" />
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
                      <input type="checkbox" class="checkbox" v-model="userData.have_disability" />
                      <span class="ml-3 text-success" v-if="userData.have_disability">SI, Especifique</span>
                      <span class="ml-3 text-info" v-else>Ninguna</span>
                    </div>
                    <div class="md:col-span-3" v-if="userData.have_disability">
                      <label for="type_disability">Tipo de discapacidad</label>
                      <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        v-model="userData.type_disability">
                        <option select>Seleccione...</option>
                        <option value="MOTRIZ">MOTRIZ</option>
                        <option value="AUDITIVA">AUDITIVA</option>
                        <option value="VISUAL">VISUAL</option>
                        <option value="INTELECTUAL">INTELECTUAL</option>
                        <option value="OTRA">OTRA</option>
                      </select>
                    </div>
                    <div class="md:col-span-3" v-if="userData.have_disability">
                      <label for="disability_persent">Porcentaje</label>
                      <input type="number" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        placeholder="Su Teléfono" v-model="userData.disability_persent" />
                    </div>
                    <div class="md:col-span-3" v-if="userData.have_disability">
                      <label for="card_conadis">Nro de Carnet</label>
                      <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                        placeholder="Su Teléfono" v-model="userData.card_conadis" />
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
                <div class="grid gap-4 gap-y-2 grid-cols-1 md:grid-cols-6">
                  <div class="md:col-span-3">
                    <label for="level_education">Nivel de Educación</label>
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      v-model="userData.level_education">
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
                    <select class="input input-sm input-secondary focus:input-primary w-full md:h-10"
                      v-model="userData.profesion">
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
                    <section class="flex flex-col items-start">
                    <span>Hoja de Vida:</span>
                    <div class="flex gap-4">
                      <a class="badge"
                        :class="urlCV ? 'text-green-600' : 'text-red-500'"
                        :href="urlCV ? urlCV : '#'">
                        {{ urlCV ? 'Descargar' : 'No hay Archivo'}}
                      </a>
                      <CheckIcon v-if="userData.cv" class="w-5 h-5 text-green-600"></CheckIcon>
                      <span v-if="userData.cv" class="text-green-600">Archivo cargado</span>
                    </div>
                    <input  
                    @change="handleFileUpload"
                    type="file"
                    accept="application/pdf"
                    class="input input-sm input-bordered input-secondary focus:input-primary w-full"
                    placeholder="Archivo PDF" />
                  </section>
                  </div>
                  <div class="md:col-span-6 pt-2 bg-gray-50 p-4 border rounded-md">
                    <Skills
                      :skills="userData.disipline"
                      @handleUpdateSkills="handleUpdateSkills($event)"
                    >
                  </Skills>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="grid gap-y-1 text-sm grid-cols-1 lg:grid-cols-4 pt-10 border-t border-zinc-300 mt-8">
              <div class="text-gray-700 ">
                <strong class="font-medium text-lg">Referencias Personales</strong>
                <div class="card card-side bg-base-100">
                </div>
              </div>
              <div class="lg:col-span-3">
                <div class="grid gap-4 gap-y-2 grid-cols-1">
                  <PersonalReferences/>
                </div>
              </div>
            </div>
              <div class="md:col-span-6 text-right py-20">
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
    <MapSelector v-if="showMapSelector"  @emitCoordinates="handelCoordinates" @emitCloseModal="handelModalMap"/>
    <Toast
      v-if="toastMessage.showToast" 
      :typeToast="toastMessage.typeToast"
      :statusResponse="statusResponse"
    />
    <ModalPasswordForm 
      v-if="showPasswordModal"
      @handelModalPassword="handelModalPassword"
      @changePassword="changePassword($event)"
    />
    <ModalPictureForm
      v-if="showPictureModal"
      @handelModalPicture="handelModalPicture"
      @changePicture="changePicture($event)"
    />
  </div>
</template> 