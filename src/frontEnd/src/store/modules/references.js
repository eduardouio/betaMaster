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