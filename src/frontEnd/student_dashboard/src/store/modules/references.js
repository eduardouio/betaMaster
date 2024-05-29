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
        addReference(state, reference) {
            state.references.push(reference);
            console.log('addReference');
        },
        updateReference(state, reference) {
            let index = state.references.findIndex(
                (element) => element.id_reference == reference.id_reference
            );
            state.references[index] = reference;
        },
        deleteReference(state, idReference) {
            let index = state.references.findIndex(
                (element) => element.id_reference == idReference
            );
            state.references.splice(index, 1);
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
        async updateReference({ commit, state, rootState }, reference) {
            let url = serverConfigData.urls.updatePersonalReference.replace(
                '{idPersonalReference}', reference.id_reference
            );
            let response = await serverInteractions.putData(url, reference);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                commit('updateReference', response.response);
            } else {
                rootState.statusResponse = response;
            }
            return response;
        },
        async deleteReference({ commit, state, rootState }, idReference) {
            let url = serverConfigData.urls.deletePersonalReference.replace(
                '{idPersonalReference}', idReference
            );
            let response = await serverInteractions.deleteData(url);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                commit('deleteReference', idReference);
            } else {
                rootState.statusResponse = response;
            }
            return response;
        },
        async createReference({ commit, state, rootState }, reference) {
            let url = serverConfigData.urls.addPersonalReference;
            let response = await serverInteractions.postData(url, reference);
            if (response.status.is_success) {
                rootState.statusResponse = response;
                commit('addReference', response.response);
            } else {
                rootState.statusResponse = response;
            }
            return response;
        }
    },
    getters:{
        getReferences(state, getters, rootState){
            return state.references;
        },
    },
};

export default module;