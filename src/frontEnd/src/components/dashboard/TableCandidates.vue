<template>
    <div
        class="relative flex flex-col min-w-0 mb-4 lg:mb-0 break-words bg-gray-50 dark:bg-gray-800 w-full shadow-lg rounded">
        <div class="rounded-t mb-0 px-0 border-0">
            <div class="flex flex-wrap items-center px-4 py-2">
                <div class="relative w-full max-w-full flex-grow flex-1">
                    <h3 class="font-semibold text-base text-gray-900 dark:text-gray-50">Mis Candidatos</h3>
                </div>
            </div>
            <div class="text-center font-semibold text-blue-500 p-10">Sin Candidatos</div>
            <div class="block w-full overflow-x-auto" v-if="false">
                <table class="items-center w-full bg-transparent border-collapse">
                    <thead>
                        <tr>
                            <th
                                class="px-4 bg-gray-100 dark:bg-gray-600 text-gray-500 dark:text-gray-100 align-middle border border-solid border-gray-200 dark:border-gray-500 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                Aspirante</th>
                            <th
                                class="px-4 bg-gray-100 dark:bg-gray-600 text-gray-500 dark:text-gray-100 align-middle border border-solid border-gray-200 dark:border-gray-500 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                Ciudad</th>
                            <th
                                class="px-4 bg-gray-100 dark:bg-gray-600 text-gray-500 dark:text-gray-100 align-middle border border-solid border-gray-200 dark:border-gray-500 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left min-w-140-px">

                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="text-gray-700 dark:text-gray-100">
                            <td class="px-4 py-3">
                                <div class="flex items-center text-sm">
                                    <div class="relative hidden w-8 h-8 mr-3 rounded-full md:block">
                                        <img class="object-cover w-full h-full rounded-full"
                                            src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-0.3.5&amp;q=80&amp;fm=jpg&amp;crop=entropy&amp;cs=tinysrgb&amp;w=200&amp;facepad=3&amp;fit=facearea&amp;s=707b9c33066bf8808c934c8ab394dff6"
                                            alt="" loading="lazy" />
                                        <div class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true">
                                        </div>
                                    </div>
                                    <div>
                                        <p class="font-semibold">CHRISTINA MARIA MELO SEGOVIA</p>
                                        <p class="text-xs text-gray-600 dark:text-gray-400">Colegio Menor Marcelo
                                            Mendez</p>
                                    </div>
                                </div>
                            </td>
                            <td
                                class="border-t-0 px-4 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                                <div class="flex items-center">
                                    <span class="mr-2">QUITO</span>
                                </div>
                            </td>
                            <td>
                                <a class="flex items-center font-medium text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-500"
                                    href="#0" style="outline: none;">
                                    Revisar <span><svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor"
                                            class="transform transition-transform duration-500 ease-in-out">
                                            <path fill-rule="evenodd"
                                                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                                clip-rule="evenodd"></path>
                                        </svg></span>
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>