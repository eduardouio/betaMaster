import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

const module = {
    state:{
        profile: null,
        picture: null,
        cv: null,
    },
    mutations: {
        setProfile(state, profile) {
            state.profile = profile;
        },
        setPicture(state, picture) {
            state.picture = picture;
        },
        setCV(state, cv) {
            state.cv = cv;
        }
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
        async fetchProfileFile({ commit, state, rootState }, type) {
            let url = serverConfigData.urls.uploadProfilePicture.replace(
                '{type}', type
            );
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                if (type === 'picture'){
                    if (response.response.url) {
                        commit('setPicture', serverConfigData.baseUrl +  response.response.url);
                    }
                }else{
                    if (response.response.url) {
                        commit('setCV', serverConfigData.baseUrl +  response.response.url);
                    }
                }
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                rootState.statusResponse = response;
            }
            return response;
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
        async updateProfileImage({ commit, state, rootState }, formData) {
            let url = serverConfigData.urls.uploadProfilePicture.replace(
                '{type}', 'upload'
            );
            let response = await serverInteractions.postFile(url, formData);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                commit('setPicture', serverConfigData.baseUrl +  response.response.url);
            } else {
                rootState.statusResponse = response;
            }
            return response;
        },
        async updateProfilePasswod({ commit, state, rootState }, userData) {
            let url = serverConfigData.urls.updatePasswordUser;
              const response = await serverInteractions.putData(
                url, JSON.stringify(userData)
            );
            rootState.statusResponse = response;
        },
    },
    getters:{
        getProfile(state, getters, rootState, rootGetters){
            return state.profile;
        },
        getPicture(state, getters, rootState, rootGetters){
            return state.picture;
        },
        getCV(state, getters, rootState, rootGetters){
            return state.cv;
        },
    },
};

export default module;