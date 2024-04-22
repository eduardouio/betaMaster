import serverConfigData from "@/config";
import serverInteractions from "@/server-interactions";

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
            let url = serverConfigData.urls.getUserBankAccount;
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                console.log('fecthBankAccounts');
                commit('setBankAccounts', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
            
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