import { createStore, storeKey } from "vuex";
import references from "@/store/modules/references.js";
import students from "@/store/modules/students.js";
import bankAccounts from "@/store/modules/bankAccounts.js";
import profile from "@/store/modules/profile.js";


export default createStore({
    state: {
        isLoading: true,
        stagesLoaded: 0,
    },  
    mutations: {
        setIsLoading(state, status) {
            state.isLoading = status;
        },
    },
    getters: {
        getIsLoading(state) {
            return state.isLoading;
        },
    },
    modules: {
        profile,
        bankAccounts,
        students,
        references,
    },
});