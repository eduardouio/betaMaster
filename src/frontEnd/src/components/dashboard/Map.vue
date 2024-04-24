<script setup>
import { ref, onMounted } from 'vue';
import "leaflet/dist/leaflet.css";
import * as L from 'leaflet';

const props = defineProps({
    locations: {
        type: String,
        required: true
    }
});

const coordinates = ref(null);

onMounted(()=> {
    coordinates.value = props.locations.split(',').map(Number);
    var map = L.map('mymap').setView(coordinates.value, 15);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);
    var marker = L.marker(coordinates.value).addTo(map);
});
</script>
<template>
   <div id="mymap" class="h-full w-full"></div>
</template>

