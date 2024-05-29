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
        async fetchCourses({ commit, state, rootState }){
            let url = serverConfigData.urls.studentData;
            console.log('Error');
            console.log(url);
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setCourses', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
        },
    },
    getters:{
        getCourses(state, getters, rootState, rootGetters){
            return state.courses;
        },
    },
};

export default module;
