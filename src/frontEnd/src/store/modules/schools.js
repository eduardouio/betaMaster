import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";


const module = {
    state:{
        schools: null,
        students: null,
    },
    mutations: {
        setSchools(state, schools) {
            state.schools = schools;
        },
        setStudents(state, students) {
            state.students = students;
        },
    },
    actions:{
        async fetchSchools({ commit, state, rootState }) {
            let url = serverConfigData.urls.teacherSchools;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                console.log('fecthSchools');
                commit('setSchools', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
        },
        async fetchStudentsBySchoolTeacher({ commit, state, rootState }, idSchool) {
            rootState.isLoading = true;
            let url = serverConfigData.urls.getStudentsBySchoolTeacher.replace('{idSchool}', idSchool);
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                console.log('fecthStudentsBySchoolTeacher');
                commit('setStudents', response.response);
                rootState.isLoading = false;
            } else {
                alert('Error en el servidor');
            }
        },
        async updateSchool({ commit, state, rootState }, userData) {
        },
        async deleteSchool({ commit, state, rootState }, userData) {
        },
        async createSchool({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getSchools(state, getters, rootState, rootGetters){
            return state.schools;
        },
        getStudentsBySchoolTeacher(state, getters, rootState){
            return state.students;
        },
    },

};

export default module;

