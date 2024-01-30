<script setup>
import { UserGroupIcon } from '@heroicons/vue/24/outline';
import { BuildingLibraryIcon } from '@heroicons/vue/24/outline';
import { BookOpenIcon } from '@heroicons/vue/24/outline';

const props = defineProps({
    nameCard: {
        type: String,
        required: true
    },
    totalCard: {    
        type: Number,
        required: true
    }
});

</script>
<template>
    <div>
        <div class="px-6 py-6 border border-blue-200 rounded-lg shadow-md">
            <div class="flex items-center justify-between">
                <span class="font-bold text-sm text-primary">{{ nameCard }}</span>
            </div>
            <div class="flex items-center justify-between mt-6">
                <div>
                    <UserGroupIcon v-if="nameCard==='Estudiantes'" class="w-12 h-12 text-info"/>
                    <BuildingLibraryIcon v-if="nameCard==='Colegios'" class="w-12 h-12 text-info"/>
                    <BookOpenIcon v-if="nameCard==='Cursos'" class="w-12 h-12 text-info"/>
                </div>
                <div class="flex flex-col">
                    <div class="flex items-end">
                        <span class="text-2xl 2xl:text-3xl font-bold text-gray-600 uppercase">{{ totalCard }} {{nameCard}}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>