import serverConfigData from "@/config.js";
import serverInteractions from "@/server-interactions";

const module = {
    state:{
        teachers: null,
    },
    mutations: {
        setTeachers(state, students) {
            state.teachers = students;
        }
    },
    actions:{
        async fetchTeachers({ commit, state, rootState }) {
            console.log('fetchTeachers');
            let url = serverConfigData.urls.getUsers;
            url = url.replace('{roleName}', 'teacher');
            let response = await serverInteractions.getData(url);
            if (response.status.is_success) {
                commit('setTeachers', response.response);
                rootState.stagesLoaded = rootState.stagesLoaded + 1;
            } else {
                alert('Error en el servidor');
            }
        }
    },
    getters:{
        getTeachers(state){
            return state.teachers.results;
        },
    },
};

export default module;