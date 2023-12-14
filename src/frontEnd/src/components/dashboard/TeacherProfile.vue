<script setup>
import { RouterLink } from 'vue-router';
</script>
<template>
    <div>
        <div class="h-full bg-gray-200 p-8">
            <div class="bg-white rounded-lg shadow-xl pb-8">
                <div class="w-full h-[250px]">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/profile-background.jpg"
                        class="w-full h-full rounded-tl-lg rounded-tr-lg">
                </div>
                <div class="flex flex-col items-center -mt-20">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/profile.jpg"
                        class="w-40 border-4 border-white rounded-full">
                    <div class="flex items-center space-x-2 mt-2">
                        <p class="text-2xl">Eduardo Vinicio Villota Montenegro</p>
                        <span class="bg-blue-500 rounded-full p-1" title="Verified">
                            <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-100 h-2.5 w-2.5" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M5 13l4 4L19 7">
                                </path>
                            </svg>
                        </span>
                    </div>
                    <p class="text-gray-700">MSC ING Tutor</p>
                    <p class="text-sm text-gray-500">Quito-Ecuador</p>
                </div>
                <div class="flex-1 flex flex-col items-center lg:items-end justify-end px-8 mt-2">
                    <div class="flex items-center space-x-4 mt-2">
                        <button
                            class="flex items-center bg-blue-600 hover:bg-blue-700 text-gray-100 px-4 py-2 rounded text-sm space-x-2 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                <path
                                    d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z">
                                </path>
                            </svg>
                            <RouterLink to="/dashboard-teacher/teacher-profile-form"><span>Modificar Perfil</span></RouterLink>
                        </button>
                    </div>
                </div>
            </div>
            <div class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
                <div class="w-full flex flex-col 2xl:w-3/5">
                    <div class="flex-1 bg-white rounded-lg shadow-xl p-7">
                        <h4 class="text-xl text-gray-900 font-bold">Información Personal</h4>
                        <ul class="mt-2 text-gray-700">
                            <li class="flex border-y py-2">
                                <span class="font-bold w-2/5">Nombre:</span>
                                <span class="text-gray-700">Villota Montenegro Eduardo Vinicio</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">F Nacimiento:</span>
                                <span class="text-gray-700">24 Jul, 1991 (30 años)</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Joined:</span>
                                <span class="text-gray-700">10 Jan 2022 (25 days ago)</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Celular:</span>
                                <span class="text-gray-700">09 992 936569</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Email:</span>
                                <span class="text-gray-700">amandaros@sexample.com</span>
                            </li>
                            <li class="flex border-b py-2">
                                <span class="font-bold w-2/5">Ubicación:</span>
                                <span class="text-gray-700">Quito-Ecuador</span>
                            </li>
                            <li class="flex items-center border-b py-2 space-x-2">
                                <span class="font-bold w-2/5">Mis Redes:</span>
                                <a href="#" title="Twitter">
                                    <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 333333 333333"
                                        shape-rendering="geometricPrecision" text-rendering="geometricPrecision"
                                        image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd">
                                        <path
                                            d="M166667 0c92048 0 166667 74619 166667 166667s-74619 166667-166667 166667S0 258715 0 166667 74619 0 166667 0zm90493 110539c-6654 2976-13822 4953-21307 5835 7669-4593 13533-11870 16333-20535-7168 4239-15133 7348-23574 9011-6787-7211-16426-11694-27105-11694-20504 0-37104 16610-37104 37101 0 2893 320 5722 949 8450-30852-1564-58204-16333-76513-38806-3285 5666-5022 12109-5022 18661v4c0 12866 6532 24246 16500 30882-6083-180-11804-1876-16828-4626v464c0 17993 12789 33007 29783 36400-3113 845-6400 1313-9786 1313-2398 0-4709-247-7007-665 4746 14736 18448 25478 34673 25791-12722 9967-28700 15902-46120 15902-3006 0-5935-184-8860-534 16466 10565 35972 16684 56928 16684 68271 0 105636-56577 105636-105632 0-1630-36-3209-104-4806 7251-5187 13538-11733 18514-19185l17-17-3 2z"
                                            fill="#1da1f2"></path>
                                    </svg>
                                </a>
                                <a href="#" title="LinkedIn">
                                    <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 333333 333333"
                                        shape-rendering="geometricPrecision" text-rendering="geometricPrecision"
                                        image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd">
                                        <path
                                            d="M166667 0c92048 0 166667 74619 166667 166667s-74619 166667-166667 166667S0 258715 0 166667 74619 0 166667 0zm-18220 138885h28897v14814l418 1c4024-7220 13865-14814 28538-14814 30514-1 36157 18989 36157 43691v50320l-30136 1v-44607c0-10634-221-24322-15670-24322-15691 0-18096 11575-18096 23548v45382h-30109v-94013zm-20892-26114c0 8650-7020 15670-15670 15670s-15672-7020-15672-15670 7022-15670 15672-15670 15670 7020 15670 15670zm-31342 26114h31342v94013H96213v-94013z"
                                            fill="#0077b5"></path>
                                    </svg>
                                </a>                               
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="flex flex-col w-full 2xl:w-2/3">
                    <div class="flex-1 bg-white rounded-lg shadow-xl p-8">
                        <h4 class="text-xl text-gray-900 font-bold">About</h4>
                        <div class="mt-2 text-gray-900">
                            <p>Es un placer dirigirme a usted para presentarme y compartir algunos aspectos importantes sobre mi personalidad y mi enfoque hacia el aprendizaje. Mi nombre es [Tu Nombre], y soy un/a estudiante dedicado/a que participa activamente en el programa de educación en el hogar.</p>
                            <p>Desde una edad temprana, he desarrollado un amor por el aprendizaje, y considero que cada día es una oportunidad para adquirir nuevos conocimientos. Mi enfoque educativo se basa en la autenticidad, la curiosidad y el compromiso con mis estudios. Siempre he creído que la educación no solo se limita al aula, sino que también se encuentra en las experiencias cotidianas y en la exploración del mundo que nos rodea.</p>
                            <p>En mis estudios, me esfuerzo por ser proactivo/a y asumir la responsabilidad de mi propio aprendizaje. Tengo un fuerte interés en [menciona áreas de interés o materias favoritas], y estoy emocionado/a de profundizar mis conocimientos en estos campos. Además, estoy abierto/a a nuevas ideas y perspectivas que enriquezcan mi experiencia educativa.</p>
                        </div>
                    </div>

            </div>
        </div>
        <div class="bg-white rounded-lg shadow-xl p-8">
            <div class="flex items-center justify-between">
                <h4 class="text-xl text-gray-900 font-bold">Connections (12)</h4>
            </div>
            <div
                class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-8 gap-8 mt-8">
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection1.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Diane Aguilar</p>
                    <p class="text-xs text-gray-500 text-center">UI/UX Design at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection2.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Frances Mather</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer at Facebook</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection3.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Carlos Friedrich</p>
                    <p class="text-xs text-gray-500 text-center">Front-End Developer at Tailwind CSS</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection4.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Donna Serrano</p>
                    <p class="text-xs text-gray-500 text-center">System Engineer at Tesla</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection5.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Randall Tabron</p>
                    <p class="text-xs text-gray-500 text-center">Software Developer at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection6.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">John McCleary</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer at Laravel</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection7.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Amanda Noble</p>
                    <p class="text-xs text-gray-500 text-center">Graphic Designer at Tailwind CSS</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection8.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Christine Drew</p>
                    <p class="text-xs text-gray-500 text-center">Senior Android Developer at Google</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection9.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Lucas Bell</p>
                    <p class="text-xs text-gray-500 text-center">Creative Writer at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection10.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Debra Herring</p>
                    <p class="text-xs text-gray-500 text-center">Co-Founder at Alpine.js</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection11.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Benjamin Farrior</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer Lead at Microsoft</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection12.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Maria Heal</p>
                    <p class="text-xs text-gray-500 text-center">Linux System Administrator at Twitter</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection13.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Edward Ice</p>
                    <p class="text-xs text-gray-500 text-center">Customer Support at Instagram</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection14.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Jeffery Silver</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer at Twitter</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection15.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Jennifer Schultz</p>
                    <p class="text-xs text-gray-500 text-center">Project Manager at Google</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600"
                    title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection16.jpg"
                        class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Joseph Marlatt</p>
                    <p class="text-xs text-gray-500 text-center">Team Lead at Facebook</p>
                </a>
            </div>
        </div>
    </div>
</div></template>