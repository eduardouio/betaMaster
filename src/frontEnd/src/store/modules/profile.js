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
            console.log("fetchProfile");
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