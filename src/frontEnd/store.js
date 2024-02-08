import { createStore } from "vuex";

export default createStore({
    state: {
        userData: null,
        dashboardData: null,
        studentData:null,
    },
    mutations: {
        setUserData(state, userData) {
            state.userData = userData;
        },
        setDashboardData(state, dashboardData) {
            state.dashboardData = dashboardData;
        },
        setStudentData(state, studentData) {
            state.studentData = studentData;
        }
    },
    actions: {
        setUserData({ commit }, userData) {
            commit('setUserData', userData);
        },
        setDashboardData({ commit }, dashboardData) {
            commit('setDashboardData', dashboardData);
        },
        setStudentData({ commit }, studentData) {
            commit('setStudentData', studentData);
        }
    },
    getters: {
        getUserData(state) {
            return state.userData;
        },
        getDashboardData(state) {
            return state.dashboardData;
        },
        getStudentData(state) {
            return state.studentData;
        }
    }
});