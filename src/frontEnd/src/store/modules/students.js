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
        async fetchStudents({ commit, state, rootState }) {
            let url = serverConfigData.urls.teacherStudents;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setStudents', response.response);
                rootState.stagesLoaded += 1;
            } else {
                alert('Error en el servidor');
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
        getStudents(state, getters, rootState, rootGetters){
            return state.students;
        },
    },
};

export default module;