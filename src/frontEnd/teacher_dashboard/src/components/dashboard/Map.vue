<script setup>
import { ref, onMounted } from 'vue';
import "leaflet/dist/leaflet.css";
import { map, tileLayer, marker } from 'leaflet';

const props = defineProps({
    locations: {
        type: String,
        required: true
    }
});

const coordinates = ref(null);

onMounted(()=> {
    coordinates.value = props.locations.split(',').map(Number);
    var mymap = map('mymap').setView(coordinates.value, 15);
    tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(mymap);
    var mymarker = marker(coordinates.value).addTo(mymap);
});
</script>
<template>
   <div id="mymap" class="h-full w-full border border-blue-400"></div>
</template>

