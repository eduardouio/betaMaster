import { createStore } from "vuex";
import references from "@/store/modules/references.js";
import students from "@/store/modules/students.js";
import bankAccounts from "@/store/modules/bankAccounts.js";
import profile from "@/store/modules/profile.js";
import scholls from "@/store/modules/schools.js";
import courses from "@/store/modules/courses.js";


export default createStore({
    state: {
        isLoading: true,
        stagesLoaded: 0,
    },  
    mutations: {
        setIsLoading(state, status) {
            console.log('setIsLoading', status);
            state.isLoading = status;
        },
    },
    getters: {
        getIsLoading(state) {
            return state.isLoading;
        },
        getStagesLoaded(state) {
            return state.stagesLoaded;
        }
    },
    modules: {
        profile,
        bankAccounts,
        students,
        references,
        scholls,
        courses,
    },
});