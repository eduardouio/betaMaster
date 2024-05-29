<script setup>
import { computed, onMounted, ref } from 'vue';
import { useStore } from 'vuex';
import { XCircleIcon, MapPinIcon } from '@heroicons/vue/24/outline';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import LoaderVue from '@/components/generics/Loader.vue';
import Map from '@/components/dashboard/Map.vue';
import imageSchoolDefault from '@/assets/school-pic.png';

const store  = useStore();
const isLoading = computed(() => store.getters.getIsLoading);
const students = computed(() => store.getters.getStudentsBySchoolTeacher);
const emits = defineEmits(['closeModal']);
const urlMap = ref('https://www.google.com/maps/search/?api=1&query=');

onMounted(() => {
    document.title = 'Colegio | Dashboard';
    store.dispatch('fetchStudentsBySchoolTeacher', props.school.id_school);

});

function emitCloseModal() {
    emits('closeModal');
}

const props = defineProps({
    school: {
        type: Object,
        required: true
    }
});

</script>
<template>
  <div class="text-sm md:text-md">
    <dialog class="modal bg-gray-100/90" open>
      <div class="modal-box p-3 border border-rounded border-sky-600 border-l-8 w-10/12 max-w-5xl">
        <div class="flex">
          <span class="w-full inline-block text-center text-sm text-cyan-800 bg- p-1">
            (#{{ school.id }}) Información De Institución
          </span>
          <XCircleIcon @click="emitCloseModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
        </div>
        <div class="flex flex-col items-center xl:flex-row xl:items-start">
          <div class="flex flex-col">
            <div class="w-96 bg-base-100">
              <div class="flex flex-col items-center">
                <span class="card-title p-1 uppercase text-info text-sm">
                  {{ school.name }} 
                </span>
              
              <figure class="w-2/4">
                <img class="rounded-md"
              :src="school.logo ? school.logo : imageSchoolDefault"
              :alt="school.name" />
              </figure>
            </div>
            </div>
           
            <hr class="mt-4">
            <ul>
              <li class="flex gap-2 flex-row items-start">
                <SocialIcon v-if="school.url_facebook"
                  :url="school.url_facebook" :icon="'facebook'" />
                <SocialIcon v-if="school.url_linkedin"
                  :url="school.url_linkedin" :icon="'linkedin'" />
                <SocialIcon v-if="school.url_instagram"
                  :url="school.url_instagram" :icon="'instagram'" />
                <SocialIcon v-if="school.url_twiter" :url="school.url_twiter"
                  :icon="'twitter'" />
              </li>
            </ul>
          </div>

          <div class="flex flex-row px-10 w-full md:flex-col">
            <ul class="text-gray-700 text-wrap md:text-nowrap">
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Contacto:</span>
                <section class="text-gray-700 flex">
                  <small class="text-gray-300">
                  </small>
                  {{ school.name_contact }} 
                </section>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Web/Tel:</span>
                <span class="text-gray-700">
                    <a :href="'tel:' + school.phone">
                        {{ school.phone }}
                    </a>
                    <small class="text-gray-400"> / </small>
                    <a :href="'https://' + school.website" target="_blank">
                        {{ school.website }}
                    </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Correo Colegio:</span>
                <span class="text-gray-700">
                  <a :href="'mailto:' + school.email">
                    {{ school.email }}
                  </a>
                </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Codigo AMI:</span>
                <span class="text-gray-700"> {{ school.ami_code }} </span>
              </li>
              <li class="flex flex-col items-start md:flex-row md:items-start border-y py-1">
                <span class="font-semibold w-2/5">Direccion:</span>
                <span class="text-gray-700 flex flex-row">
                  <a :href="urlMap+school.geolocation" target="_blank">
                    <MapPinIcon class="w-5 h-5 text-primary" />
                  </a>
                  {{ school.state }},
                  {{ school.city }},
                  <br/>
                  {{ school.address }}
                </span>
              </li>
            </ul>
          </div>
        </div>
        <div class="flex h-[300px]" v-if="school.geolocation">
          <Map :locations="school.geolocation"/>
        </div>
        <div class="flex flex-col">
          <LoaderVue v-if="isLoading"/>
          <span class="text-gray-700 ">Datos Históricos:</span>
          <div className="overflow-x-auto">
            <table class="table table-xs table-border">
            <thead>
              <tr class="bg-gray-200 text-center text-gray-950">
                <th>#</th>
                <th>Estudiante</th>
                <th>Email</th>
                <th>Ciudad</th>
                <th>Telefono</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(student, idx) in students" class=" hover:bg-yellow-50" :key="student.email">
                <td>{{ idx + 1 }}</td>
                <td>{{ student.first_name }} {{ student.last_name }}</td>
                <td>{{ student.email }}</td>
                <td>{{ student.state }},{{ student.city}} </td>
                <td>{{ student.phone }}</td>
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
