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
            let url = serverConfigData.urls.getSchools;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setSchools', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
        },
    },
    getters:{
        getSchools(state, getters, rootState, rootGetters){
            return state.schools;
        },
    },

};

export default module;
