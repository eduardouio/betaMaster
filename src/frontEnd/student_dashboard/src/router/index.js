import { createRouter, createWebHashHistory } from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';
import HomeDashboard from '@/components/dashboard/sections/HomeDashboard.vue';
import SchoolsList from '@/components/dashboard/sections/SchoolsList.vue';
import StudentsList from '@/components/dashboard/sections/StudentsList.vue';
import StudentProfile from '@/components/dashboard/sections/StudentProfile.vue';
import StudentProfileForm from '@/components/dashboard/sections/StudentProfileForm.vue';


const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      component: Dashboard,
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
          component: StudentProfile,
        },
        {
          path: 'edit/',
          component: StudentProfileForm,
        },
      ],
    }
  ]
})

export default router
