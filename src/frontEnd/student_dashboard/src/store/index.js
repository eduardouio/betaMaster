import { createStore } from "vuex";
import profile from "@/store/modules/profileStudent.js";
import courses from "@/store/modules/coursesStudent.js";
import schools from "@/store/modules/schoolsStudent.js";


const store =  createStore({
  state: {
    isLoading: true,
    stagesLoaded: 0,
    statusResponse: null,
  },
  mutations: {
    setIsLoading(state, status) {
      console.log("setIsLoading", status);
      state.isLoading = status;
    },
    incrementCounter(state) {
      state.stagesLoaded = state.stagesLoaded + 1;
    },
    enableLoader(state) {
      state.isLoading = true;
    },
    disableLoader(state) {
      state.isLoading = false;
    },
  },
  getters: {
    getIsLoading(state) {
      return state.isLoading;
    },
    getStagesLoaded(state) {
      return state.stagesLoaded;
    },
    getStatusResponse(state) {
      return state.statusResponse;
    },
  },
  modules: {
    profile,
    courses,
    schools,
  },
});

export default store;