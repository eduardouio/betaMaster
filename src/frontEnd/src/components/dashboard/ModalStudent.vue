<script setup>
import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import serverConfigData from '@/config';
import LoaderVue from '@/components/generics/Loader.vue';
import { XMarkIcon, MapPinIcon } from '@heroicons/vue/24/outline';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import imageMenDefault from '@/assets/profile-pic-men.png';
import imageWomanDefault from '@/assets/profile-pic-woman.png';

const store = useStore();
const emits = defineEmits(['closeModal']);
let showLoader = ref(true);
let studentDataByTeacher = null;

const props = defineProps({
    idStudent: {
        type: String,
        required: true,
        default: ''
    }
});

const classsStatus = {
    'POR INICIAR': 'text-sky-900 md:w-1/2',
    'EN PROCESO': 'text-green-900 md:w-1/2',
    'FINALIZADO': 'text-red-900 md:w-1/2'
};

const imageDefault = ref('');

onMounted(() => {
    loadData();
});

function emitCloseModal() {
    showLoader.value = true;
    emits('closeModal');
}

// Cargamos los datos del etudiante seleccionado
async function loadData() { 
    console.log('Estamos cargaando los datos del estudiante');
    console.log('idStudent' +  props.idStudent);
    let url = serverConfigData.urls.studentDataByteacher.replace(
        '{idStudent}', props.idStudent
    );

    url = url.replace(
        '{idTeacher}', serverConfigData.idUser
    );
  
    let response = await fetch(
        url,{
        method: 'GET',
        headers: serverConfigData.headers
    });

    if (response.status != 200){
        console.log('Error al cargar los datos del estudiante');
        console.log(response);
    } else {
        store.commit('setStudentDataByTeacher', await response.json());
        studentDataByTeacher = await store.state.studentDataByTeacher;
        imageDefault.value = studentDataByTeacher.student.sex === 'hombre'? imageMenDefault : imageWomanDefault;
        showLoader.value = false;
    }
}
</script>
<style scoped>
.my-modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8); /* Fondo semi-transparente */
}

</style>
<template>
  <div class="my-modal">
    <LoaderVue v-if="showLoader" />
    <dialog v-else class="modal" open>
      <div class="modal-box w-10/12 max-w-5xl">
        <span class="text-sm text-gray-400"> (#{{ studentDataByTeacher.student.id }}) | </span>
        <span class="rounded-md p-1 text-xl uppercase text-info">
          {{ studentDataByTeacher.student.first_name }} {{ studentDataByTeacher.student.last_name }}
        </span>
        <div class="flex flex-col items-center xl:flex-row xl:items-start rounded-md bg-white p-6">
          <div class="flex flex-col items-center ">
            <img class="w-40 h-40 rounded-md object-cover"
              :src="studentDataByTeacher.student.first_name.picture ? studentDataByTeacher.student.first_name.picture : imageDefault"
              :alt="studentDataByTeacher.student.first_name" />
            <hr class="mt-4">
            <ul>
              <li class="flex gap-3 flex-col md:flex-row">
                <SocialIcon v-if="studentDataByTeacher.student.url_facebook"
                  :url="studentDataByTeacher.student.url_facebook" :icon="'facebook'" />
                <SocialIcon v-if="studentDataByTeacher.student.url_linkedin"
                  :url="studentDataByTeacher.student.url_linkedin" :icon="'linkedin'" />
                <SocialIcon v-if="studentDataByTeacher.student.url_instagram"
                  :url="studentDataByTeacher.student.url_instagram" :icon="'instagram'" />
                <SocialIcon v-if="studentDataByTeacher.student.url_twiter" :url="studentDataByTeacher.student.url_twiter"
                  :icon="'twitter'" />
              </li>
            </ul>
          </div>

          <div class="flex flex-row px-10 w-full md:flex-col">
            <ul class="text-gray-700 text-wrap md:text-nowrap">
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Colegio:</span>
                <section class="text-gray-700 flex">
                  <small class="text-gray-300">
                  </small>
                  <a href="geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                  {{ studentDataByTeacher.active_courses[0].school.name }}
                  <small class="text-gray-400">
                    (
                    #{{ studentDataByTeacher.active_courses[0].school.id }}
                    )
                  </small>
                </section>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Nacionalidad:</span>
                <span class="text-gray-700">{{ studentDataByTeacher.student.nationality }}
                  <small class="text-gray-300">|</small>
                  {{ studentDataByTeacher.student.civil_status }}
                  <small class="text-gray-300">|</small>
                  <span class="badge capitalize"
                    :class="studentDataByTeacher.student.sex === 'mujer' ? 'text-pink-800' : 'text-green-800'">
                    {{ studentDataByTeacher.student.sex }}
                  </span>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Correo estudiante:</span>
                <span class="text-gray-700">
                  <a :href="'mailto:' + studentDataByTeacher.student.email">
                    {{ studentDataByTeacher.student.email }}
                  </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Correo Colegio:</span>
                <span class="text-gray-700">
                  <a :href="'mailto:' + studentDataByTeacher.active_courses[0].school.email">
                    {{ studentDataByTeacher.active_courses[0].school.email }}
                  </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Nacionalidad:</span>
                <span class="text-gray-700">{{ studentDataByTeacher.student.nationality }}<small
                    class="text-gray-300">|</small>
                  {{ studentDataByTeacher.student.civil_status }}
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Nro Cedula:</span>
                <span class="text-gray-700"> {{ studentDataByTeacher.student.dni_number }} </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Discapacidad:</span>
                <span class="text-gray-700"> {{ studentDataByTeacher.student.have_disability ? 'SI' : 'NO' }}
                  <small class="badge bg-cyan-50" v-if="studentDataByTeacher.student.have_disability">
                    {{ studentDataByTeacher.student.type_disability }} {{ studentDataByTeacher.student.disability_persent }} %
                    Carnet:
                    {{ studentDataByTeacher.student.card_conadis }}
                  </small>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Direccion:</span>
                <span class="text-gray-700 flex flex-row">
                  <a href="geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                  {{ studentDataByTeacher.student.state }},
                  {{ studentDataByTeacher.student.city }},
                  {{ studentDataByTeacher.student.address }}
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Direccion Colegio:</span>
                <span class="text-gray-700 flex flex-row">
                  <a href="geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                  {{ studentDataByTeacher.active_courses[0].school.state }},
                  {{ studentDataByTeacher.active_courses[0].school.city }},
                  {{ studentDataByTeacher.active_courses[0].school.address }}
                </span>
              </li>
            </ul>
          </div>
        </div>
        <div class="flex flex-col">
          <span class="text-gray-700">Datos Históricos:</span>
          <table class="table table-border">
            <thead>
              <tr class="bg-gray-200 text-center text-gray-950">
                <th>#</th>
                <th>Peridodo</th>
                <th>Colegio</th>
                <th>Ciudad</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(value, idx) in studentDataByTeacher.active_courses" class=" hover:bg-yellow-50" :key="value">
                <td>{{ idx + 1 }}</td>
                <td>{{ value.active_course.period }}</td>
                <td>{{ value.school.name }}</td>
                <td>
                  {{ studentDataByTeacher.active_courses[0].school.state }},
                  {{ studentDataByTeacher.active_courses[0].school.city }}
                </td>
                <td>
                  <div :class="classsStatus[value.active_course.state]">
                    {{ value.active_course.state }}
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="modal-action">
          <form method="dialog">
            <button class="btn btn-sm btn-error btn-outline hover:text-white" @click="emitCloseModal">
            <XMarkIcon class="w-4 h-4" />
            Cerrar
          </button>
        </form>
      </div>
    </div>
  </dialog>
</div></template>