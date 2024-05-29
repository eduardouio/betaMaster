import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

const module = {
    state:{
        students: null,
        studentData: null,
    },
    mutations: {
        setStudents(state, students) {
            state.students = students;
        },
        setStudentData(state, studentData) {
            state.studentData = studentData;
        },
        setNullStudentData(state){
            state.studentData = null;
        }
    },
    actions:{
        async fetchStudents({ commit, state, rootState }) {
            let url = serverConfigData.urls.teacherStudents;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                console.log('fetchStudents');
                commit('setStudents', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
        },
        async fetchStudentData({commit, state, rootState}, idStudent){
            console.log('Cargamos info del estudiante');
            let url = serverConfigData.urls.studentDataByteacher.replace(
               '{idStudent}', idStudent 
            ).replace(
                '{idTeacher}', serverConfigData.idUser
            );
            let response = await serverInteractions.getData(url)
            if(response.status.is_success){
                commit('setStudentData', response.response);
                rootState.isLoading = false;
            }
        },
        async updateStudent({ commit, state, rootState }, userData) {
        },
        async deleteStudent({ commit, state, rootState }, userData) {
        },
        async createStudent({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getStudents(state){
            return state.students;
        },
        getStudentData(state){
            return state.studentData;
        },
    },
};

export default module;