// archivos  de configuracion del frontEnd

const csrfToken = 'kjhgfdertyukmnbv';
const baseUrl = 'http://localhost:8000';
//usuario profesor
const idUser = 359;

const serverConfigData = {
    'csrfToken': csrfToken,
    'idUser': idUser,
    'headers':{
        'Content-Type': 'application/json',
        'Accept': 'application/json',
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
        registerUser : baseUrl + '/api/user/add/', // POST
        loginUser : baseUrl + '/login/', // POST
        logoutUser : baseUrl + '/logout/', // GET
        updateUser : baseUrl + '/api/user/update-password/{idUser}/', // PUT
        getUser : baseUrl + '/api/user/{idUser}/', // GET
        getUsers : baseUrl + '/api/user/users-by-role/{roleName}/', // GET
        updateUser : baseUrl + '/api/user/update/{idUser}/', // PUT
        teacherData: baseUrl + '/api/user/complete-data-teacher/{idUser}/', // GET
        studentData: baseUrl + '/api/user/complete-data-student/{idUser}/', // GET
        // cursos activos
        getActiveCourse : baseUrl + '/api/active-course/{idActiveCourse}/', // GET
        getActiveCourses : baseUrl + '/api/active-courses/', // GET
        // cuentas bancarias
        getBankAccount : baseUrl + '/api/bank-account/{idBankAccount}/', // GET
        addBankAccount : baseUrl + '/api/bank-account/add/', // POST
        deleteBankAccount : baseUrl + '/api/bank-account/delete/{idBankAccount}/', // DELETE
        updateBankAccount : baseUrl + '/api/bank-account/update/{idBankAccount}/', // PUT
        // pagos subscripciones
        addPaymentSubscription : baseUrl + '/api/payment-subscription/add/', // POST
        updatePaymentSubscription : baseUrl + '/api/payment-subscription/update/{idPaymentSubscription}/', // PUT
        getPaymentSubscription : baseUrl + '/api/payment-subscription/{idPaymentSubscription}/', // GET
        // referencias personales
        addPersonalReference : baseUrl + '/api/personal-reference/add/', // POST
        updatePersonalReference : baseUrl + '/api/personal-reference/update/{idPersonalReference}/', // PUT
        deletePersonalReference : baseUrl + '/api/personal-reference/delete/{idPersonalReference}/', // DELETE
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