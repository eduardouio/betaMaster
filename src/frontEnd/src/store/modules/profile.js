import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

const module = {
    state:{
        profile: null,
    },
    mutations: {
        setProfile(state, profile) {
            state.profile = profile;
        },
    },
    actions:{
        async fetchProfile({ commit, state, rootState }) {
            let url = serverConfigData.urls.getUser;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setProfile', response.response);
                rootState.stagesLoaded += 1;
            } else {
                alert('Error en el servidor');
            }
        },
        async updateProfile({ commit, state, rootState }, userData) {
        },
        async deleteProfile({ commit, state, rootState }, userData) {
        },
        async createProfile({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getProfile(state, getters, rootState, rootGetters){
            return state.profile;
        },
    },
};

export default module;