import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

const module = {
    state:{
        references: null,
    },
    mutations: {
        setReferences(state, references) {
            state.references = references;
        },
    },
    actions:{
        async fetchReferences({ commit, state, rootState }) {
            let url = serverConfigData.urls.getAllPersonalReferences;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                console.log('fecthReferences');
                commit('setReferences', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
            
        },
        async updateReference({ commit, state, rootState }, userData) {
        },
        async deleteReference({ commit, state, rootState }, userData) {
        },
        async createReference({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getReferences(state, getters, rootState, rootGetters){
            return state.references;
        },
    },
};

export default module;