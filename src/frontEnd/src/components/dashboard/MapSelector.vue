<script setup>
import {ref, onMounted, computed} from 'vue';
import { useStore } from 'vuex';
import { XCircleIcon } from '@heroicons/vue/24/outline';
import "leaflet/dist/leaflet.css";
import * as L from 'leaflet';
import LoaderVue from '@/components/generics/Loader.vue';


const store = useStore();
const emits = defineEmits(['emitCloseModal', 'emitCoordinates']);
const isLoading = ref(true);

const emitCloseModal = () => {
    emits('emitCloseModal');
};

const emitCoordinates = (coordinates) => {
    coordinates = coordinates.join(',');
    emits('emitCoordinates', coordinates);
};

onMounted(()=>{
    getGeoLocation();
});


const getGeoLocation = function () {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(drawMAp);
    } else {
        drawMAp([-0.1876557, -78.517207]);
        alert("Geolocation is not supported by this browser.");
    }
};

const drawMAp = function(position, automate = true){
    isLoading.value = false;
    var coordinates = null;
    
    if (automate){
        coordinates = [position.coords.latitude, position.coords.longitude];
    }else{
        coordinates = position;
    } 
    
    document.getElementById('mapContainer').innerHTML = `<div id="mymap" class="h-full w-full border border-blue-400"></div>`;
    emitCoordinates(coordinates);
    var map = L.map('mymap').setView(coordinates, 14);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);
    if (automate){
        var marker = L.marker(coordinates).addTo(map);
    }else{
      var marker = L.marker(position).addTo(map);
    }
    map.on('click', onMapClick);

};

const onMapClick = function (e){
  drawMAp(Object.values(e.latlng), false);
}

</script>
<template>
    <div class="text-sm md:text-md">
    <dialog class="modal bg-gray-100/90" open>
    <LoaderVue v-if="isLoading" />
      <div class="modal-box p-3 border border-rounded border-sky-600 border-l-8 w-10/12 max-w-5xl">
        <div class="flex">
          <span class="w-full inline-block text-center text-sm text-cyan-800 bg- p-1">
            Marque Su Ubicación en em Mapa
          </span>
          <XCircleIcon @click="emitCloseModal" class="w-5 h-5 text-red-600 hover:text-red-900 hover:border" />
        </div>
        <div class="h-[300px] w-full" id="mapContainer">
        </div> 
        <div class="modal-action">
          <form method="dialog">
            <button class="btn btn-sm btn-outline btn-info hover:text-white">
              <XCircleIcon class="w-5 h-5" />
              Cerrar
            </button>
          </form>
        </div>
      </div>
    </dialog>
  </div>
</template>