import { createStore } from "vuex";

export default createStore({
    state: {
        userData: null,
        dashboardData: null,
        studentDataByTeacher:null,
    },
    mutations: {
        setUserData(state, userData) {
            state.userData = userData;
        },
        setDashboardData(state, dashboardData) {
            state.dashboardData = dashboardData;
        },
        setStudentDataByTeacher(state, studentDataByTeacher) {
            state.studentDataByTeacher = studentDataByTeacher;
        }
    },
    actions: {
        setUserData({ commit }, userData) {
            commit('setUserData', userData);
        },
        setDashboardData({ commit }, dashboardData) {
            commit('setDashboardData', dashboardData);
        },
        setStudentDataByTeacher({ commit }, studentDataByTeacher) {
            commit('setstudentDataByTeacher', studentDataByTeacher);
        }
    },
    getters: {
        getUserData(state) {
            return state.userData;
        },
        getDashboardData(state) {
            return state.dashboardData;
        },
        getStudentDataByTeacher(state) {
            return state.studentDataByTeacher;
        }
    }
});