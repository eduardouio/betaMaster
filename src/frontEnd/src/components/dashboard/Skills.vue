<template>
    <div>
        <span class="text-gray-600"> Seleccionado: <small class="text-info">(Clic para eliminar)</small></span>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 md:pt-4">
            <ul v-for="item in selectedSkills" :key="item.name">
                <li @click="item.selected = false"
                    class="bg-gray-200 flex justify-between p-1 gap-2 border border-slate-300 rounded-md hover:shadow-lg">
                    <div class="flex gap-2">
                        <span class="w-2" :class="item.color"></span>
                        <span v-text="item.name" class="uppercase text-sm"></span>
                    </div>
                    <XCircleIcon class="w-4 h-4 text-error" />
                </li>

            </ul>
        </div>
        <hr class="m-3" />
        <span class="text-gray-600">Disponibles: <small class="text-info">(Click para agregar)</small></span>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 md:pt-4">
            <ul v-for="item in unselectedSkills" :key="item.name">
                <li @click="item.selected = true"
                    class="bg-gray-200 flex justify-between p-1 gap-2 border border-slate-300 rounded-md hover:shadow-lg">
                    <div class="flex gap-2">
                        <span class="w-2" :class="item.color"></span>
                        <span v-text="item.name" class="uppercase text-sm"></span>
                    </div>
                    <CheckCircleIcon class="w-4 h-4 text-success" />
                </li>
            </ul>
        </div>

    </div>
</template>
<script setup>
import { defineProps, onMounted, ref, computed } from 'vue'
import { CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/outline';

const selectedSkills = computed(() => {
    return all_skills.value.disiplinas.filter(i => i.selected);
})

const unselectedSkills = computed(() => {
    return all_skills.value.disiplinas.filter(i => !i.selected);
})

const all_skills = ref({
    disiplinas: [
        { name: "Química", selected: true, color: "bg-lime-500" },
        { name: "Matemáticas", selected: false, color: "bg-emerald-500" },
        { name: "Física", selected: false, color: "bg-teal-500" },
        { name: "Biologia", selected: false, color: "bg-sky-500" },
        { name: "Lengua y Liretura", selected: false, color: "bg-yellow-500" },
        { name: "Matematicas", selected: false, color: "bg-blue-500" },
        { name: "Filosofía", selected: false, color: "bg-rose-500" },
        { name: "Inglés", selected: false, color: "bg-purple-500" },
        { name: "Ciencias Sociales", selected: false, color: "bg-indigo-500" },
        { name: "Historia", selected: false, color: "bg-pink-500" },
    ],
});

const props = defineProps({
    skills: {
        type: String,
        required: true
    }
})

onMounted(() => {
    console.log('init skills component');
})

</script>