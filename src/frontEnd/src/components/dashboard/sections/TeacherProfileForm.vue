<script setup>
import { useStore } from 'vuex';
import { onMounted, ref, watch } from 'vue';
import provincias from '@/assets/provincias.json';
import LoaderVue from '@/components/generics/Loader.vue';
import { CheckBadgeIcon, ExclamationTriangleIcon } from '@heroicons/vue/24/outline';

const store = useStore();
const showLoader = ref(true);
let states = ref([]);
let cities = ref([]);
let parroquias = ref([]);
let userData = null;
const sexo = ref(['HOMBRE', 'MUJER', 'OTRO']);

onMounted(async() => {
  userData = await store.state.userData;
  states = Object.values(provincias).map(item => item.provincia);
  cities = Object.values(
    Object.values(provincias).filter(
      item=>item.provincia===userData.user.state)[0].cantones
      ).map(item=>item.canton);
  parroquias =  Object.values(
    Object.values(
      Object.values(provincias).filter(
        item=>item.provincia===userData.user.state)[0].cantones
        ).map(item=>item).filter(
          item => item.canton===userData.user.city)[0].parroquias);
  if (userData) {
    showLoader.value = false;
  }
});
</script>
<template>
  <div>
    <LoaderVue v-if="showLoader"/>
    <div v-else class="p-1 bg-base flex items-center justify-center border rounded-md">
      <div class="max-w-screen-xl mx-auto">
        <div>
          <div class="grid grid-cols-1 lg:grid-cols-4">
            <div class="lg:col-span-2"><h2 class="font-semibold text-xl text-gray-700">Actualización de Perfil</h2></div>
            <div class="lg:col-span-2 text-end">
              <span v-if="userData.user.is_aproved" class="badge rounded-md p-2 pl-3 pr-3 text-error hover:bg-error hover:text-white">
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
                <div class="card card-side">
                  <figure><img
                      src="https://img.freepik.com/foto-gratis/chico-guapo-seguro-posando-contra-pared-blanca_176420-32936.jpg"
                      alt="Movie" class="w-2/3 h:auto" /></figure>
                </div>
              </div>
              <div class="lg:col-span-3 mt-5">
                <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-6">
                  <div class="md:col-span-3">
                    <label for="full_name">
                      <strong class="text-red-500">*</strong>
                      Nombres
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Nombres"
                      v-model="userData.user.first_name"
                    />
                  </div>
                  <div class="md:col-span-3">
                    <label for="full_name">
                      <strong class="text-red-500">*</strong>
                      Apellidos
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Apellidos"
                      v-model="userData.user.last_name"
                    />
                  </div>
                  <div class="md:col-span-3">
                    <label for="full_name">
                      <strong class="text-red-500">*</strong>
                      Identificación
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Identificación"
                      v-model="userData.user.dni_number"
                    />
                  </div>
                  <div class="md:col-span-3">
                    <label for="full_name">
                      <strong class="text-red-500">*</strong>
                      Sexo
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Nombres"
                      v-model="userData.user.sex"
                    />
                  </div>
                  <div class="md:col-span-3">
                    <label for="full_name">
                      <strong class="text-red-500">*</strong>
                      Pais
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Apellidos"
                      v-model="userData.user.country"
                      readonly
                    />
                  </div>  
                  <div class="md:col-span-3">
                    <label for="address">
                      <strong class="text-red-500">*</strong>
                      Correo Electronico:
                      <small v-if="userData.user.is_confirmed_mail" class="badge rounded-md p-2 pl-3 pr-3 text-error hover:bg-error hover:text-white">
                        <ExclamationTriangleIcon class="h-4 w-4 inline-block" /> 
                        &nbsp;Pendiente
                      </small>
                      <small v-else class="badge rounded-md p-2 pl-3 pr-3 text-green-800 hover:text-white hover:bg-green-800">
                        <CheckBadgeIcon class="h-4 w-4 inline-block" />
                        &nbsp;Correo Verificado
                      </small>
                    </label>
                    <input
                      type="email"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="nombre@dominio.com"
                      v-model="userData.user.email"
                      readonly
                    />
                  </div>
                  <di v class="md:col-span-3">
                    <label for="zipcode">
                      <strong class="text-red-500">*</strong>
                      Fecha de Nacimiento
                    </label>
                    <input
                      type="date"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Nacimiento"
                      v-model="userData.user.date_of_birth"
                      />
                  </di>
                  <div class="md:col-span-3">
                    <label for="zipcode">
                      <strong class="text-red-500">*</strong>
                      Geolocalización
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Ubicación"
                      v-model="userData.user.geolocation"
                    />
                  </div>
                  <div class="md:col-span-4">
                    <label for="email">
                      <strong class="text-red-500">*</strong>
                      Dirección:
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Dirección"
                      v-model="userData.user.address"
                      />
                  </div>
                  <div class="md:col-span-2">
                    <label for="city">
                      <strong class="text-red-500">*</strong>
                      Pais
                    </label>
                    <input
                      type="text"
                      maxlength="13"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Pais"
                      v-model="userData.user.country"
                    />
                  </div>
                  <div class="md:col-span-2">
                    <label for="country">
                      <strong class="text-red-500">*</strong>
                      Provincia
                    </label>
                    <div class="h-10 bg-gray-50 flex border border-gray-200 rounded items-center mt-1">
                      <select 
                        class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                        v-model="userData.user.state"
                        >
                        <option 
                          v-for="item in states"
                          v-text="item"
                          :value="item"
                          :key="item">
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="md:col-span-2">
                    <label for="state">
                      <strong class="text-red-500">*</strong>
                      Cantón
                    </label>
                    <div class="h-10 bg-gray-50 flex border border-gray-200 rounded items-center mt-1">
                      <select 
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      v-model="userData.user.city"
                      >
                        <option
                          v-for="item in cities"
                          :key="item"
                          :value="item" 
                          v-text="item"
                        >
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="md:col-span-2">
                    <label for="zipcode">
                      <strong class="text-red-500">*</strong>
                      Parroquia
                    </label>
                    <select
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      v-model="userData.user.parroquia"
                    >
                      <option 
                        v-for="item in parroquias"
                        :key="item"
                        :value="item"
                        v-text="item"
                      >
                      </option>
                    </select>
                  </div>
                  <div class="md:col-span-2">
                    <label for="zipcode">
                      <strong class="text-red-500">*</strong>
                      Celular
                    </label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Celular"
                      v-model="userData.user.phone"
                    />
                  </div>
                  <div class="md:col-span-2">
                    <label for="zipcode">Tel Fijo</label>
                    <input
                      type="text"
                      class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Su Teléfono"
                      v-model="userData.user.phone_2"
                      />
                  </div>
                  <div class="md:col-span-2">
                    <label for="zipcode"><strong class="text-red-500">*</strong> Código ZIP</label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11" />
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
                  <div class="md:col-span-6">
                    <label for="full_name">Hoja de Vida PDF</label>
                    <input type="file" class="input input-sm input-bordered input-secondary focus:input-primary w-full"
                      placeholder="Sus Nombres" />
                  </div>
                  <div class="md:col-span-6">
                    <label for="zipcode"><strong class="text-red-500">*</strong> Acerca de Mi</label>
                    <textarea class="input input-sm input-secondary focus:input-primary w-full h-30"></textarea>
                  </div>
                  <div class="md:col-span-6">
                    <label for="">Referencias</label>
                    <div class="overflow-x-auto">
                      <table class="table">
                        <!-- head -->
                        <thead class="text-gray-600">
                          <tr>
                            <th>#</th>
                            <th>Institución</th>
                            <th>Contacto</th>
                            <th>Estado</th>
                          </tr>
                        </thead>
                        <tbody>
                          <!-- row 1 -->
                          <tr>
                            <th>1</th>
                            <td>Cy Ganderton</td>
                            <td>Quality Control Specialist</td>
                            <td class="text-error">Rechazado</td>
                          </tr>
                          <!-- row 2 -->
                          <tr class="hover">
                            <th>2</th>
                            <td>Hart Hagerty</td>
                            <td>Desktop Support Technician</td>
                            <td class="text-success">Verificado</td>
                          </tr>
                          <!-- row 3 -->
                          <tr>
                            <th>3</th>
                            <td>Brice Swyre</td>
                            <td>Tax Accountant</td>
                            <td class="text-success">Verificado</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
              <div class="md:col-span-6 text-right py-5">
                <div class="inline-flex items-end">
                  <button class="btn btn-primary text-white">Actualizar Información</button>
                </div>
              </div>
            </div>
            <div class="grid gap-y-1 text-sm grid-cols-1 lg:grid-cols-4 pt-10 border-t border-zinc-300 mt-8">
              <div class="text-gray-700 ">
                <strong class="font-medium text-lg">Acciones de cuenta</strong>
                <div class="card card-side bg-base-100">
                </div>
              </div>
              <div class="lg:col-span-3">
                <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-6">
                  <div class="md:col-span-3">
                    <label for="full_name">Contraseña</label>
                    <input type="text" class="input input-sm input-bordered input-secondary focus:input-primary w-full"
                      placeholder="Sus Nombres" />
                  </div>
                  <div class="md:col-span-3">
                    <label for="full_name">Repita Contraseña</label>
                    <input type="text" class="input input-sm input-secondary focus:input-primary w-full md:h-11"
                      placeholder="Sus Apellidos" />
                  </div>
                  <div class="md:col-span-6 text-right py-5">
                    <div class="inline-flex items-end">
                      <button class="btn btn-primary text-white">Actualizar Contraseña</button>
                    </div>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>