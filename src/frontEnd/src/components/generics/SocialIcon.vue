<script setup>
const props = defineProps(
    {
        url: String,
        icon: String,
    }
);

const iconsTypes = {
    facebook: `<svg class="h-5 w-5" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path fill="#1877F2" d="M15 8a7 7 0 00-7-7 7 7 0 00-1.094 13.915v-4.892H5.13V8h1.777V6.458c0-1.754 1.045-2.724 2.644-2.724.766 0 1.567.137 1.567.137v1.723h-.883c-.87 0-1.14.54-1.14 1.093V8h1.941l-.31 2.023H9.094v4.892A7.001 7.001 0 0015 8z"></path><path fill="#ffffff" d="M10.725 10.023L11.035 8H9.094V6.687c0-.553.27-1.093 1.14-1.093h.883V3.87s-.801-.137-1.567-.137c-1.6 0-2.644.97-2.644 2.724V8H5.13v2.023h1.777v4.892a7.037 7.037 0 002.188 0v-4.892h1.63z"></path></g></svg>`,
    twitter: `<svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" width="24px" height="24px" viewBox="0 0 24 24" style="enable-background:new 0 0 24 24;" xml:space="preserve"><path d="M14.095479,10.316482L22.286354,1h-1.940718l-7.115352,8.087682L7.551414,1H1l8.589488,12.231093L1,23h1.940717  l7.509372-8.542861L16.448587,23H23L14.095479,10.316482z M11.436522,13.338465l-0.871624-1.218704l-6.924311-9.68815h2.981339  l5.58978,7.82155l0.867949,1.218704l7.26506,10.166271h-2.981339L11.436522,13.338465z"/></svg>`,
    instagram: `<svg class="h-5 w-5" viewBox="0 0 14 14" role="img" focusable="false" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <radialGradient id="a" cx="130.802" cy="895.86902" r="968.776" gradientTransform="matrix(.539 -.842 .618 .395 -492.923 652.145)" gradientUnits="userSpaceOnUse"> <stop offset="0" stop-color="#F9ED32"></stop> <stop offset=".53" stop-color="#FF4700"></stop> <stop offset=".72" stop-color="#EE2A7B"></stop> <stop offset="1" stop-color="#002AFF"></stop> </radialGradient> <path fill="url(#a)" d="M43.7 180h524.6c24.2 0 43.7 19.6 43.7 43.7v524.6c0 24.2-19.6 43.7-43.7 43.7H43.7C19.6 792 0 772.4 0 748.3V223.7C0 199.6 19.6 180 43.7 180z" transform="translate(1.000001 -2.5294102) scale(.0196)"></path> <g fill="#ffffff" stroke="#ffffff" stroke-miterlimit="10" transform="translate(1.000001 -2.5294102) scale(.0196)"> <path stroke-width="8" d="M413.9 721.5H198.1c-70.3 0-127.6-57.2-127.6-127.6V378.1c0-70.3 57.2-127.6 127.6-127.6H414c70.3 0 127.6 57.2 127.6 127.6V594c-.1 70.3-57.3 127.5-127.7 127.5zM198.1 289.8c-48.7 0-88.3 39.6-88.3 88.3V594c0 48.7 39.6 88.3 88.3 88.3H414c48.7 0 88.3-39.6 88.3-88.3V378.1c0-48.7-39.6-88.3-88.3-88.3H198.1zm107.9 314c-64.9 0-117.8-52.8-117.8-117.8 0-64.9 52.8-117.8 117.8-117.8 64.9 0 117.8 52.8 117.8 117.8 0 64.9-52.9 117.8-117.8 117.8zm0-196.3c-43.3 0-78.5 35.2-78.5 78.5s35.2 78.5 78.5 78.5 78.5-35.2 78.5-78.5-35.2-78.5-78.5-78.5z"></path> <circle cx="427.70001" cy="364.29999" r="25" stroke-width="9"></circle> </g> </g></svg>`,
    linkedin: `<svg  class="h-6 w-6" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path fill="#0A66C2" d="M12.225 12.225h-1.778V9.44c0-.664-.012-1.519-.925-1.519-.926 0-1.068.724-1.068 1.47v2.834H6.676V6.498h1.707v.783h.024c.348-.594.996-.95 1.684-.925 1.802 0 2.135 1.185 2.135 2.728l-.001 3.14zM4.67 5.715a1.037 1.037 0 01-1.032-1.031c0-.566.466-1.032 1.032-1.032.566 0 1.031.466 1.032 1.032 0 .566-.466 1.032-1.032 1.032zm.889 6.51h-1.78V6.498h1.78v5.727zM13.11 2H2.885A.88.88 0 002 2.866v10.268a.88.88 0 00.885.866h10.226a.882.882 0 00.889-.866V2.865a.88.88 0 00-.889-.864z"></path></g></svg>`,
};

</script>
<template>
    <a 
    :href="url" 
    :title="'Ver perfil en ' + icon"
    target="_blank" 
    v-html="iconsTypes[icon]"
    class="pl-1 hover:transform hover:scale-110"
    ></a>
</template>