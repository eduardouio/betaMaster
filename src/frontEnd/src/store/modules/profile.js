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
                console.log('fecthProfile');
                commit('setProfile', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                rootState.statusResponse = response;
            }
        },
        async updateProfile({ commit, state, rootState }, userData) {
            let url = serverConfigData.urls.updateUser;
            let response = await serverInteractions.putData(url, userData);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                commit('setProfile', response.response);
            } else {
                rootState.statusResponse = response;
            }
            return response;
        },
        async updateProfileImage({ commit, state, rootState }, userData) {
            let url = serverConfigData.urls.uploadProfilePicture;
            let response = await serverInteractions.postFile(url, userData);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                commit('setProfile', response.response);
            } else {
                rootState.statusResponse = response;
            }
            return response;
        },
        async updateProfilePasswod({ commit, state, rootState }, userData) {

        }
    },
    getters:{
        getProfile(state, getters, rootState, rootGetters){
            return state.profile;
        },
    },
};

export default module;