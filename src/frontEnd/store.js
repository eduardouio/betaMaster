import { createStore } from "vuex";

export default createStore({
    state: {
        userData: null,
        dashboardData: null,
    },
    mutations: {
        setUserData(state, userData) {
            state.userData = userData;
        },
        setDashboardData(state, dashboardData) {
            state.dashboardData = dashboardData;
        }
    },
    actions: {
        setUserData({ commit }, userData) {
            commit('setUserData', userData);
        },
        setDashboardData({ commit }, dashboardData) {
            commit('setDashboardData', dashboardData);
        }
    },
    getters: {
        getUserData(state) {
            return state.userData;
        },
        getDashboardData(state) {
            return state.dashboardData;
        }
    }
});