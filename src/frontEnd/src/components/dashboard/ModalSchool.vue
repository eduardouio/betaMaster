<script setup>
import { ref, onMounted } from 'vue';
import { XMarkIcon, MapPinIcon } from '@heroicons/vue/24/outline';
import SocialIcon from '@/components/generics/SocialIcon.vue';
import imageDefault from '@/assets/logo.jpeg';


const emits = defineEmits(['closeModal']);

function emitCloseModal() {
    emits('closeModal');
}
let showModal = ref(true);

const props = defineProps({
    school: {
        type: Object,
        required: true
    }
});

const classsStatus = {
    'POR INICIAR': 'text-sky-900 md:w-1/2',
    'EN PROCESO': 'text-green-900 md:w-1/2',
    'FINALIZADO': 'text-red-900 md:w-1/2'
};
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
    <dialog v-if="showModal" class="modal" open>
      <div class="modal-box w-10/12 max-w-5xl">
        <span class="text-sm text-gray-400"> (#{{ school.school.id }}) | </span>
        <span class="rounded-md p-1 text-xl uppercase text-info">
          {{ school.school.name }} 
        </span>
        <div class="flex flex-col items-center xl:flex-row xl:items-start rounded-md bg-white p-6">
          <div class="flex flex-col items-center ">
            <img class="w-40 h-40 rounded-md object-cover"
              :src="school.school.logo ? school.school.logo : imageDefault"
              :alt="school.school.name" />
            <hr class="mt-4">
            <ul>
              <li class="flex gap-3 flex-col md:flex-row">
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
          <span class="text-gray-700">Datos Históricos:</span>
          <table class="table table-border">
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
                    <span v-for="aCourse in value.courses">
                        <ul>
                            <li><small class="text-gray-400">(#{{ aCourse.id_active_courses }})</small> {{ aCourse.period }} | {{ aCourse.state }}</li>
                        </ul>
                    </span>
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
  </div>
</template>
