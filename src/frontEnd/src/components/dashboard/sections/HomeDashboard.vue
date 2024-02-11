<script setup>
import CardIndicator from '@/components/dashboard/CardIndicator.vue';
import TableStudents from '@/components/dashboard/TableStudents.vue';
import ModalStudent from '@/components/dashboard/ModalStudent.vue';
import { useStore } from 'vuex';
import { ref, reactive, onMounted } from 'vue';

const store = useStore();
let showModal = ref(false);
let idStudent = ref('0');
const counter = reactive({
    schools: [],
    students: [],
    courses: []
});

function handleIdStudent(id) {
    idStudent.value = id.toString();
    showModal.value = true;
};

function handelModal() {
    showModal.value = false;
}

onMounted(async () => {
    const dashboardData = await store.state.dashboardData;
    counterItems(dashboardData);
    document.title = 'Inicio | Dashboard';
});

function counterItems(data) {
    data.forEach((item) => {
        counter.schools.push(item.school.id);
        counter.students.push(item.student.id);
        counter.courses.push(item.active_course.id_active_courses);
    });
    counter.schools = counter.schools.filter((val, idx, array) => array.indexOf(val) === idx);
    counter.students = counter.students.filter((val, idx, array) => array.indexOf(val) === idx);
    counter.courses = counter.courses.filter((val, idx, array) => array.indexOf(val) === idx);
}

</script>
<template>
    <div>
        <div class="grid items-center grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 ">
            <CardIndicator :nameCard="'Cursos'" :totalCard="counter.courses.length" />
            <CardIndicator :nameCard="'Estudiantes'" :totalCard="counter.students.length" />
            <CardIndicator :nameCard="'Colegios'" :totalCard="counter.schools.length" />
        </div>
        <div class="grid grid-cols-1 p-4 gap-4">
            <TableStudents @idStudent="handleIdStudent" />
        </div>
        <ModalStudent v-if="showModal" :idStudent="idStudent" @closeModal="handelModal" />
    </div>
</template>
