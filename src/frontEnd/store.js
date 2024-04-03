import { createStore, storeKey } from "vuex";
import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

export default createStore({
    state: {
        userData: null,
        dashboardData: null,
        studentDataByTeacher:null,
        statusResponse: null,
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
        },
        setStatusResponse(state, statusResponse) {
            state.statusResponse = statusResponse;
        }
    },
    actions: {
        async updateProfile({ commit }, userData) {
            let url = serverConfigData.urls.updateUser.replace('{idUser}',
                serverConfigData.idUser
            );
            userData = userData.user;
            delete(userData.cv);
            delete(userData.picture);
            let response = await serverInteractions.putData(url, userData.user); 
            commit('setStatusResponse', response.status);
            if (response.status.is_success) {
                commit('setUserData', userData);
            }
            return userData;
        },
    },
    getters: {
        getReferences(state){
            return state.userData.references;
        },
        getUserData(state) {
            return state.userData;
        },
        getDashboardData(state) {
            return state.dashboardData;
        },
        getStudentDataByTeacher(state) {
            return state.studentDataByTeacher;
        },
        getStatusResponse(state) {
            return state.statusResponse;
        }
    }
});