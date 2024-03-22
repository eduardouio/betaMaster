<template>
    <div>
        <span class="text-gray-600"> Seleccionado: <small class="text-info">(Clic para eliminar)</small></span>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 md:pt-4">
            <ul v-for="item in selectedSkills" :key="item.name">
                <li @click="updateSkills(item)"
                    class="bg-gray-200 flex justify-between p-1 gap-2 border border-slate-300 rounded-md hover:shadow-lg">
                    <div class="flex gap-2">
                        <span class="w-1" :class="item.color"></span>
                        <span v-text="item.name" class="uppercase text-sm"></span>
                    </div>
                    <XCircleIcon class="w-4 h-4 text-error" />
                </li>

            </ul>
        </div>
        <hr class="m-3" />
        <span class="text-gray-600">Disponibles: <small class="text-info">(Clic para agregar)</small></span>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 md:pt-4">
            <ul v-for="item in unselectedSkills" :key="item.name">
                <li @click="updateSkills(item)"
                    class="bg-gray-200 flex justify-between p-1 gap-2 border border-slate-300 rounded-md ">
                    <div class="flex gap-2">
                        <span class="w-1" :class="item.color"></span>
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

const emits = defineEmits(['handleUpdateSkills']);

const selectedSkills = computed(() => {
    return all_skills.value.disiplinas.filter(i => i.selected);
})

const unselectedSkills = computed(() => {
    return all_skills.value.disiplinas.filter(i => !i.selected);
})

let all_skills = ref({
    disiplinas: [
        { name: "QUÍMICA", selected: false, color: "bg-lime-500" },
        { name: "MATEMÁTICAS", selected: false, color: "bg-emerald-500" },
        { name: "FÍSICA", selected: false, color: "bg-teal-500" },
        { name: "BIOLOGÍA", selected: false, color: "bg-slate-500" },
        { name: "LENGUA Y LIRETURA", selected: false, color: "bg-yellow-500" },
        { name: "FILOSOFÍA", selected: false, color: "bg-rose-500" },
        { name: "INGLÉS", selected: false, color: "bg-purple-500" },
        { name: "CIENCIAS SOCIALES", selected: false, color: "bg-indigo-500" },
        { name: "HISTORIA", selected: false, color: "bg-pink-500" },
        { name: "EDUCACIÓN FÍSICA", selected: false, color: "bg-orange-500"},
        { name: "ÉTICA Y VALORES", selected: false, color: "bg-red-500"},
        { name: "COMPUTACIÓN", selected: false, color: "bg-cyan-500"},

    ],
});

const updateSkills = (item) => {
    item.selected = !item.selected;
    const updatesSkilld = {
        disiplinas: all_skills.value.disiplinas.filter(i => i.selected).map(i => i.name)
    }
    emits('handleUpdateSkills', JSON.stringify(updatesSkilld));
}

const props = defineProps({
    skills: {
        type: String,
        required: true
    }
})

onMounted(() => {
    const userSkills = JSON.parse(props.skills).disiplinas;
    userSkills.forEach((item) => {
        const index = all_skills.value.disiplinas.findIndex(i => i.name === item);
        if (index !== -1){
            all_skills.value.disiplinas[index].selected = true;
        }else{
            all_skills.value.disiplinas.push({
                name: item,
                selected: true,
                color: "bg-zinc-500"
            });
        }
    });
})


</script>