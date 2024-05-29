// archivos  de configuracion del frontEnd

const csrfToken = 'kjhgfdertyukmnbv';
const baseUrl = 'http://localhost:8000';
//usuario profesor
const idUser = 447;

const serverConfigData = {
    'csrfToken': csrfToken,
    'baseUrl': baseUrl,
    'idUser': idUser,
    'headers':{
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-CSRFToken': csrfToken
    },
    'headersFiles':{
        'X-CSRFToken': csrfToken
    },
    'urls': {
        // base
        baseUrl : baseUrl,
        // media
        url_media : baseUrl + '/media/',
        // auth
        login : baseUrl + '/login/', // POST
        logout : baseUrl + '/logout/', // GET
        // usuarios
        uploadCVFile : baseUrl + `/api/user/upload-cv/${idUser}/`, // POST
        uploadProfilePicture : baseUrl + `/api/user/upload-picture/${idUser}/{type}/`, // POST
        logoutUser : baseUrl + '/accounts/logout/', // GET
        updatePasswordUser : baseUrl + `/api/user/update-password/${idUser}/`, // PUT
        getUser : baseUrl + `/api/user/${idUser}/`, // GET
        getUsers : baseUrl + '/api/user/users-by-role/{roleName}/', // GET
        updateUser : baseUrl + `/api/user/update/${idUser}/`, // PUT
        teacherData: baseUrl + `/api/user/complete-data-teacher/${idUser}/`, // GET
        coursesByUser: baseUrl + `/api/user/courses-by-user/${idUser}/`, // GET
        studentData: baseUrl + `/api/user/complete-data-student/${idUser}/`, // GET
        // cursos activos
        getActiveCourse : baseUrl + '/api/active-course/{idActiveCourse}/', // GET
        getActiveCourses : baseUrl + '/api/active-courses/', // GET
        // pagos subscripciones
        addPaymentSubscription : baseUrl + '/api/payment-subscription/add/', // POST
        updatePaymentSubscription : baseUrl + '/api/payment-subscription/update/{idPaymentSubscription}/', // PUT
        getPaymentSubscription : baseUrl + '/api/payment-subscription/{idPaymentSubscription}/', // GET
        // escuelas
        addSchool : baseUrl + '/api/school/add/', // POST
        updateSchool : baseUrl + '/api/school/update/{idSchool}/', // PUT
        deleteSchool : baseUrl + '/api/school/delete/{idSchool}/', // DELETE
        getSchool : baseUrl + '/api/school/{idSchool}/', // GET
        getSchools : baseUrl + '/api/schools/', // GET
        // planes de estudio
        getStudyPlanDetail : baseUrl + '/api/study-plan-detail/{idStudyPlanDetail}/', // GET
        getStudyPlan : baseUrl + '/api/study-plan/{idStudyPlan}/', // GET
        getStudyPlans : baseUrl + '/api/study-plans/', // GET
        // suscripciones
        addSubscription : baseUrl + '/api/subscription/add/', // POST
        getSubscription : baseUrl + '/api/subscription/{idSubscription}/', // GET
        getSubscriptions : baseUrl + '/api/subscriptions/', // GET

    }
}

export default serverConfigData;
