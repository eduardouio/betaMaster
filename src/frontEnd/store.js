import { createStore } from "vuex";

export default createStore({
    state: {
        userData: null,
        userStudents: null,
        dashboardData: null,
    },
    mutations: {
        setUserData(state, userData) {
            state.userData = userData;
        },
        setUserStudents(state, userStudents) {
            state.userStudents = userStudents;
        },
        setDashboardData(state, dashboardData) {
            state.dashboardData = dashboardData;
        }
    },
    actions: {
        setUserData({ commit }, userData) {
            commit('setUserData', userData);
        },
        setUserStudents({ commit }, userStudents) {
            commit('setUserStudents', userStudents);
        },
        setDashboardData({ commit }, dashboardData) {
            commit('setDashboardData', dashboardData);
        }
    },
    getters: {
        getUserData(state) {
            return state.userData;
        },
        getUserStudents(state) {
            return state.userStudents;
        },
        getDashboardData(state) {
            return state.dashboardData;
        }
    }
});