<script setup>
import { UserGroupIcon } from '@heroicons/vue/24/outline';
import { BuildingLibraryIcon } from '@heroicons/vue/24/outline';
import { BookOpenIcon } from '@heroicons/vue/24/outline';
import { computed, reactive }  from 'vue';
import { useStore } from 'vuex';

const store = useStore();

let categories = reactive({
    courses: { name: 'Cursos', total: 0, color: 'border-blue-400'},
    students: { name: 'Estudiantes', total: 0, color: 'border-orange-400'},
    schools: { name: 'Instituciones', total: 0, color: 'border-yellow-400'},
});

const counter = computed(()=>{
    if (props.nameCard === 'courses'){
        return store.getters.getCourses.length;
    };
    if (props.nameCard === 'students') {
        return store.getters.getStudents.length;
    }
    if (props.nameCard === 'schools') {
        return store.getters.getSchools.length;
    }
});

const props = defineProps({
    nameCard: {
        type: String,
        required: true
    }
});

</script>
<template>
    <div>
        <div class="px-2 py-2 rounded-md border-l-8 border hover:border-slate-400 shadow-md" :class="categories[nameCard].color">
            <div class="flex items-center justify-between">
                <span class="text-xl font-light text-cyan-600">{{ categories[nameCard].name }}</span>
            </div>
            <div class="flex items-center justify-between mt-6">
                <div>
                    <UserGroupIcon v-if="nameCard === 'students'" class="w-12 h-12 font-light" />
                    <BuildingLibraryIcon v-if="nameCard === 'courses'" class="w-12 h-12 font-light" />
                    <BookOpenIcon v-if="nameCard === 'schools'" class="w-12 h-12 font-light" />
                </div>
                <div class="flex flex-col">
                    <div class="flex items-end gap-2">
                        <span class="text-2xl 2xl:text-3xl font-bold text-gray-600 uppercase">
                            {{ counter }}
                        </span>
                        <span class="text-2xl">
                            {{ categories[nameCard].name }}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
