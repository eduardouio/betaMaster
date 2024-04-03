const module = {
    state:{
        bankAccounts: null,
    },
    mutations: {
        setBankAccounts(state, bankAccounts) {
            state.bankAccounts = bankAccounts;
        },
    },
    actions:{
        async fetchBankAccounts({ commit, state, rootState}) {
            console.log("fetchBankAccounts");
            commit('setIsLoading', false, { root: true });
            console.log(rootState.isLoading);
            
        },
        async updateBankAccount({ commit, state, rootState }, userData) {
        },
        async deleteBankAccount({ commit, state, rootState }, userData) {
        },
        async createBankAccount({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getBankAccounts(state, getters, rootState, rootGetters){
            return state.bankAccounts;
        },
    },
};

export default module;