<script setup>
import { ref, reactive } from 'vue';
import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';

const v = reactive({
    url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    zoom: 15,
    center: [51.505, -0.159],
    markerLatLng: [51.504, -0.159]
});
</script>

<template>
  <l-map style="height: 300px" :zoom="ubication.zoom" :center="ubication.center">
    <l-tile-layer :url="ubication.url" :attribution="ubication.attribution"></l-tile-layer>
    <l-marker :lat-lng="ubication.markerLatLng"></l-marker>
  </l-map>
</template>
