import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";


const module = {
    state:{
        schools: null,
    },
    mutations: {
        setSchools(state, schools) {
            state.schools = schools;
        },
    },
    actions:{
        async fetchSchools({ commit, state, rootState }) {
            let url = serverConfigData.urls.teacherSchools;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setSchools', response.response);
                rootState.stagesLoaded += 1;
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
    },

};

export default module;

