const module = {
    state:{
        students: null,
    },
    mutations: {
        setStudents(state, students) {
            state.students = students;
        },
    },
    actions:{
        async fetchStudents({ commit, state, rootState }) {
            console.log("fetchStudents");
        },
        async updateStudent({ commit, state, rootState }, userData) {
        },
        async deleteStudent({ commit, state, rootState }, userData) {
        },
        async createStudent({ commit, state, rootState }, userData) {
        }
    },
    getters:{
        getStudents(state, getters, rootState, rootGetters){
            return state.students;
        },
    },
};

export default module;