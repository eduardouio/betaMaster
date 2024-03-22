<script setup>
import { ref, onMounted } from 'vue';
import { XCircleIcon, MapPinIcon } from '@heroicons/vue/24/outline';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import imageDefault from '@/assets/logo.jpeg';


const emits = defineEmits(['closeModal']);

function emitCloseModal() {
    emits('closeModal');
}

const props = defineProps({
    school: {
        type: Object,
        required: true
    }
});

const classsStatus = {
    'POR INICIAR': 'text-xs md:text-sm text-sky-900 md:w-1/2 border inline p-1 rounded-md',
    'EN PROCESO': 'text-xs md:text-sm text-green-900 md:w-1/2 border inline p-1 rounded-md',
    'FINALIZADO': 'text-xs md:text-sm text-red-900 md:w-1/2 border inline p-1 rounded-md',
};
</script>
<template>
  <div class="text-sm md:text-md">
    <dialog class="modal bg-gray-100/90" open>
      <div class="modal-box p-3 border border-rounded border-sky-600 border-l-8 w-10/12 max-w-5xl">
        <div class="flex">
          <span class="w-full inline-block text-center text-sm text-cyan-800 bg- p-1">
            (#{{ school.school.id }}) Información De Institución
          </span>
          <XCircleIcon @click="emitCloseModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
        </div>
        <div class="flex flex-col items-center xl:flex-row xl:items-start rounded-md bg-white p-6">
          <div class="flex flex-col items-center">
            <div class="card w-96 bg-base-100 shadow-md border rounded-md">
              <div class="card-body flex items-center">
                <span class="card-title p-1 uppercase text-info text-sm">
                  {{ school.school.name }} 
                </span>
              </div>
              <figure>
                <img class="w-40 h-40 rounded-md object-cover"
              :src="school.school.logo ? school.school.logo : imageDefault"
              :alt="school.school.name" />
              </figure>
            </div>
           
            <hr class="mt-4">
            <ul>
              <li class="flex gap-4 flex-row justify-between">
                <SocialIcon v-if="school.school.url_facebook"
                  :url="school.school.url_facebook" :icon="'facebook'" />
                <SocialIcon v-if="school.school.url_linkedin"
                  :url="school.school.url_linkedin" :icon="'linkedin'" />
                <SocialIcon v-if="school.school.url_instagram"
                  :url="school.school.url_instagram" :icon="'instagram'" />
                <SocialIcon v-if="school.school.url_twiter" :url="school.school.url_twiter"
                  :icon="'twitter'" />
              </li>
            </ul>
          </div>

          <div class="flex flex-row px-10 w-full md:flex-col">
            <ul class="text-gray-700 text-wrap md:text-nowrap">
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Contacto:</span>
                <section class="text-gray-700 flex">
                  <small class="text-gray-300">
                  </small>
                  <a href="geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                  {{ school.school.name_contact }} 
                </section>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Web/Tel:</span>
                <span class="text-gray-700">
                    <a :href="'tel:' + school.school.phone">
                        {{ school.school.phone }}
                    </a>
                    <small class="text-gray-400"> / </small>
                    <a :href="'https://' + school.school.website" target="_blank">
                        {{ school.school.website }}
                    </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Correo Colegio:</span>
                <span class="text-gray-700">
                  <a :href="'mailto:' + school.school.email">
                    {{ school.school.email }}
                  </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Codigo AMI:</span>
                <span class="text-gray-700"> {{ school.school.ami_code }} </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-bold w-2/5">Direccion:</span>
                <span class="text-gray-700 flex flex-row">
                  <a href="geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                  {{ school.school.state }},
                  {{ school.school.city }},
                  {{ school.school.address }}
                </span>
              </li>
            </ul>
          </div>
        </div>
        <div class="flex flex-col">
          <span class="text-gray-700 ">Datos Históricos:</span>
          <div className="overflow-x-auto">
            <table class="table table-xs table-border">
            <thead>
              <tr class="bg-gray-200 text-center text-gray-950">
                <th>#</th>
                <th>Estudiante</th>
                <th>Email</th>
                <th>Ciudad</th>
                <th>Cursos</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(value, idx) in school.students" class=" hover:bg-yellow-50" :key="value">
                <td>{{ idx + 1 }}</td>
                <td>{{ value.student.first_name }} {{ value.student.last_name }}</td>
                <td>{{ value.student.email }}</td>
                <td>{{ value.student.state }},{{ value.student.city}} </td>
                <td>
                    <span v-for="aCourse in value.courses" :key="aCourse">
                        <ul>
                            <li class="flex flex-row items-center">
                              <small class="text-gray-400 text-center" >(#{{ aCourse.id_active_courses }})</small> 
                              <p>{{ aCourse.period }}</p>
                              <span class="inline-block" :class="classsStatus[aCourse.state]">{{ aCourse.state }}</span>
                            </li>
                        </ul>
                    </span>
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
