import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import RegisterView from '../views/RegisterView.vue';
import DashBoardTeacher from '../views/DashBoardTeacher.vue';
import HomeDashboard from '../components/dashboard/sections/HomeDashboard.vue';
import SchoolsList from '../components/dashboard/sections/SchoolsList.vue';
import StudentsList from '../components/dashboard/sections/StudentsList.vue';
import TeacherProfile from '../components/dashboard/sections/TeacherProfile.vue';
import TeacherProfileForm from '../components/dashboard/sections/TeacherProfileForm.vue';
import LoginView from '../views/LoginView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/dashboard-teacher',
      component: DashBoardTeacher,
      children:[
        {
          path: '',
          component: HomeDashboard,
        },
        {
          path: 'schools/',
          component: SchoolsList,
        },
        {
          path: 'students/',
          component: StudentsList,
        },
        {
          path: 'profile/',
          component: TeacherProfile,
        },
        {
          path: 'edit/',
          component: TeacherProfileForm,
        },
      ],
    }
  ]
})

export default router
