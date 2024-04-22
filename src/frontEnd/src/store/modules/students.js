import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

const module = {
    state:{
        students: null,
    },
    mutations: {
        setStudents(state, students) {
            state.students = students;
        },
    },
    actions:{
        async fetchStudents({ commit, state, rootState, rootGetters }) {
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
        async getStudentData({commit, state, rootState}, idStudent, idTeacher){
            console.log('Cargamos info del estudiante');
            let url = serverConfigData.url.studentDataByteacher.replace(
               '{idStudent}', idStudent 
            ).replace(
                '{idTeacher}', idTeacher
            );
            let response = await serverInteractions.getData(url)

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
    },
};

export default module;