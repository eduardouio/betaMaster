<script setup>
import HeaderDashboard from '../components/dashboard/HeaderDashboard.vue';
import SideBar from '../components/dashboard/SideBar.vue';
import CardHome from '../components/dashboard/CardHome.vue';
import TableStudents from '../components/dashboard/TableStudents.vue';
import TableSchools from '../components/dashboard/TableSchools.vue';
import TableCandidates from '../components/dashboard/TableCandidates.vue';

</script>

<template>
    <div>
        <div
            class="min-h-screen flex flex-col flex-auto flex-shrink-0 antialiased bg-white dark:bg-gray-700 text-black dark:text-white">
            <HeaderDashboard/>
            <SideBar/>
            <div class="h-full ml-14 mt-14 mb-10 md:ml-64">
                <!-- Statistics Cards -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 p-4 gap-4">
                    <CardHome/>
                    <CardHome/>
                    <CardHome/>
                    <CardHome/>
                </div>
                <TableStudents/>    
                <!-- ./Statistics Cards -->
                <div class="grid grid-cols-1 lg:grid-cols-2 p-4 gap-4">
                    <!-- Social Traffic -->
                    <TableSchools/>
                    <!-- ./Social Traffic -->

                    <!-- Recent Activities -->
 <TableCandidates/>
                    <!-- ./Recent Activities -->
                </div>
            </div>
        </div>
    </div>
</template>