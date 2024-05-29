import { createRouter, createWebHistory } from 'vue-router';
import DashBoardTeacher from '@/views/DashboardTeacher.vue';
import HomeDashboard from '@/components/dashboard/sections/HomeDashboard.vue';
import SchoolsList from '@/components/dashboard/sections/SchoolsList.vue';
import StudentsList from '@/components/dashboard/sections/StudentsList.vue';
import TeacherProfile from '@/components/dashboard/sections/TeacherProfile.vue';
import TeacherProfileForm from '@/components/dashboard/sections/TeacherProfileForm.vue';


const router = createRouter({
  history: createWebHistory('/dashboard-profesor/'),
  routes: [
    {
      path: '/',
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

console.log('my error -> router/index.js');
console.dir(router);
router.beforeEach((to, from, next) => {
  console.log('Navigating to:', to.fullPath);
  next();
});


export default router
