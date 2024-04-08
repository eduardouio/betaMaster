import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";


const module = {
    state:{
        courses: null,
    },
    mutations: {
        setCourses(state, courses) {
            state.courses = courses;
        },
    },
    actions:{
        async fetchCourses({ commit, state, rootState }) {
            let url = serverConfigData.urls.coursesByUser;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setCourses', response.response);
                rootState.stagesLoaded += 1;
            } else {
                alert('Error en el servidor');
            }
        },
        async updateCourse({ commit, state, rootState }, userData) {
        },
        async deleteCourse({ commit, state, rootState }, userData) {
        },
        async createCourse({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getCourses(state, getters, rootState, rootGetters){
            return state.courses;
        },
    },
};

export default module;
