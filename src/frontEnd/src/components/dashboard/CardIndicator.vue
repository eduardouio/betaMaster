<script setup>
import { UserGroupIcon } from '@heroicons/vue/24/outline';
import { BuildingLibraryIcon } from '@heroicons/vue/24/outline';
</script>

<template>
    <div>
        <div class="px-6 py-6 bg-gray-100 border border-gray-300 rounded-lg shadow-xl">
            <div class="flex items-center justify-between">
                <span class="font-bold text-sm text-indigo-600">Estudiantes</span>
                <span
                    class="text-xs text-white bg-red-600 hover:bg-red-500 hover:text-gray-200 px-2 py-1 rounded-lg transition duration-200 cursor-default">
                    2 nuevos
                </span>
            </div>
            <div class="flex items-center justify-between mt-6">
                <div>
                    <UserGroupIcon class="w-12 h-12"/>
                </div>
                <div class="flex flex-col">
                    <div class="flex items-end">
                        <span class="text-2xl 2xl:text-3xl font-bold">12 Estudiantes</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>