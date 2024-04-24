<script setup>
  import { ref, onMounted, computed } from 'vue';
import { useStore } from 'vuex';
import LoaderVue from '@/components/generics/Loader.vue';
import { MapPinIcon, XCircleIcon } from '@heroicons/vue/24/outline';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import Map from '@/components/dashboard/Map.vue';
import imageMenDefault from '@/assets/profile-pic-men.png';
import imageWomanDefault from '@/assets/profile-pic-woman.png';

const store = useStore();
const emits = defineEmits(['closeModal']);
const isLoading = computed(() => store.getters.getIsLoading);
const studentDataByTeacher = computed(() => store.getters.getStudentData);

const props = defineProps({
    idStudent: {
        type: Number,
        required: true,
        default: 0
    }
});

const defaultImage = computed(() => {
  if (!studentDataByTeacher.value) return imageMenDefault;
  if (studentDataByTeacher.value.student.picture) return studentDataByTeacher.value.student.picture;
  return studentDataByTeacher.value.student.sex === 'MUJER' ? imageWomanDefault : imageMenDefault;
});

const classsStatus = {
    'POR INICIAR': 'text-xs md:text-sm text-sky-900 md:w-1/2 border inline md:p-1 rounded-md',
    'EN PROCESO': 'text-xs md:text-sm text-green-900 md:w-1/2 border inline md:p-1 rounded-md',
    'FINALIZADO': 'text-xs md:text-sm text-red-900 md:w-1/2 border inline md:p-1 rounded-md',
};

onMounted(() => {
  store.dispatch('fetchStudentData', props.idStudent);
});

function emitCloseModal() {
    store.commit('disableLoader');
    emits('closeModal');
}

</script>
<template>
  <div class="text-sm md:text-md">
    <LoaderVue v-if="isLoading" />
    <dialog v-else class="modal bg-gray-100/90" open="">
      <div class="modal-box p-3 border border-rounded border-sky-600 border-l-8 w-10/12 max-w-5xl">
        <div class="flex">
          <span class="w-full inline-block text-center text-cyan-800 text-xl pb-4">
            (# {{ studentDataByTeacher.student.id }}) Información De Estudiante
          </span>
          <XCircleIcon @click="emitCloseModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
        </div>
        <div class="flex flex-col xl:flex-row xl:items-start ">
          <div class="flex flex-col">
            <div class="w-60 bg-base-100 flex flex-col items-center">
              <div class="flex">
                <span class="card-title p-1 uppercase text-info text-sm">
                   {{ studentDataByTeacher.student.first_name }}  {{ studentDataByTeacher.student.last_name }}
                </span>
              </div>
              <figure class="w-3/4">
                <img class="rounded-md "
                  :src="defaultImage"
                  :alt="studentDataByTeacher.student.first_name" />
              </figure>
            </div>
            <ul class="mt-4">
              <li class="flex gap-4 flex-row justify-between">
                <SocialIcon v-if="studentDataByTeacher.student.url_facebook"
                  :url="studentDataByTeacher.student.url_facebook" icon="'facebook'" />
                <SocialIcon v-if="studentDataByTeacher.student.url_linkedin"
                  :url="studentDataByTeacher.student.url_linkedin" icon="'linkedin'" />
                <SocialIcon v-if="studentDataByTeacher.student.url_instagram"
                  :url="studentDataByTeacher.student.url_instagram" icon="'instagram'" />
                <SocialIcon v-if="studentDataByTeacher.student.url_twiter"
                  :url="studentDataByTeacher.student.url_twiter" icon="'twitter'" />
              </li>
            </ul>
          </div>
          <div class="flex flex-row px-10 w-full md:flex-col">
            <ul class="text-gray-700 text-wrap md:text-nowrap">
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Colegio:
                </span>
                <section class="text-gray-700 flex">
                  <small class="text-gray-300">
                  </small>
                   {{ studentDataByTeacher.active_courses[0].school.name }}
                  <small class="text-gray-400">
                    (
                    # {{ studentDataByTeacher.active_courses[0].school.id }}
                    )
                  </small>
              </section>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Nacionalidad:</span>
                <span class="text-gray-700"> {{ studentDataByTeacher.student.nationality }}
                  <small class="text-gray-300">|</small>
                   {{ studentDataByTeacher.student.civil_status }}
                  <small class="text-gray-300">|</small>
                  <span class="badge capitalize"
                    class2="studentDataByTeacher.student.sex === 'mujer' ? 'text-pink-800' : 'text-green-800'">
                     {{ studentDataByTeacher.student.sex }}
                  </span>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Correo estudiante:</span>
                <span class="text-gray-700">
                  <a :href="'mailto:' + studentDataByTeacher.student.email">
                     {{ studentDataByTeacher.student.email }}
                  </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Correo Colegio:</span>
                <span class="text-gray-700">
                  <a :href="'mailto:' + studentDataByTeacher.active_courses[0].school.email">
                     {{ studentDataByTeacher.active_courses[0].school.email }}
                  </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Discapacidad:</span>
                <span class="text-gray-700">  {{ studentDataByTeacher.student.have_disability ? 'SI' : 'NO' }}
                  <small class="badge bg-cyan-50" vif="studentDataByTeacher.student.have_disability">
                     {{ studentDataByTeacher.student.type_disability }} 
      {{ studentDataByTeacher.student.disability_persent
    }} %
                    Carnet:
                     {{ studentDataByTeacher.student.card_conadis }}
                  </small>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start py-1">
                <span class="font-semibold w-2/5">Direccion:</span>
                <span class="text-gray-700 flex flex-row">
                  <a :href="'https://www.google.com/maps/search/?api=1&query=' + studentDataByTeacher.student.geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                   {{ studentDataByTeacher.student.state }},
                   {{ studentDataByTeacher.student.city }},
                   <br>
                   {{ studentDataByTeacher.student.address }}
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Direccion Colegio:</span>
                <span class="text-gray-700 flex flex-row">
                  <a :href="'https://www.google.com/maps/search/?api=1&query=' +studentDataByTeacher.active_courses[0].school.geolocation " target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                   {{ studentDataByTeacher.active_courses[0].school.state }},
                   {{ studentDataByTeacher.active_courses[0].school.city }},
                   <br>
                   {{ studentDataByTeacher.active_courses[0].school.address }}
                </span>
              </li>
            </ul>
          </div>
        </div>
        <div class="flex h-[300px]" v-if="studentDataByTeacher.student.geolocation">
          <Map :locations="studentDataByTeacher.student.geolocation"/>
        </div>
        <div class="flex flex-col"> 
          <span class="text-gray-700">Datos Históricos:</span>
          <div className="overflow-x-auto">
            <table class="table table-xs table-border">
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
                <tr v-for="(value, idx) in studentDataByTeacher.active_courses" class=" hover:bg-yellow-50"
                  :key="value">
                  <td> {{ idx + 1 }}</td>
                  <td> {{ value.active_course.period }}</td>
                  <td> {{ value.school.name }}</td>
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
        </div>
        <div class="modal-action">
          <form method="dialog">
            <button class="btn btn-sm btn-outline btn-info hover:text-white" @click="emitCloseModal">
              <XCircleIcon class="w-5 h-5" />
              Cerrar
            </button>
          </form>
        </div>
      </div>
    </dialog>
  </div>
</template>