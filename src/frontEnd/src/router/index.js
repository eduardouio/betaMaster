import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import DashBoardTeacher from '../views/DashBoardTeacher.vue'
import TeacherProfile from '../components/dashboard/TeacherProfile.vue'
import TeacherProfileForm from '../components/dashboard/TeacherProfileForm.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/dashboard-teacher',
      name: 'dashboard-teacher',
      component: DashBoardTeacher,
      children:[
        {
          path: 'profile',
          component: TeacherProfile,
        },
        {
          path: 'teacher-profile-form',
          component: TeacherProfileForm,
        }
      ],
    }
  ]
})

export default router
