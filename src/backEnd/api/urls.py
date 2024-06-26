from api.GenericsViews.GenericsDetailAPIViews import (
    DetailStudyPlanAPIView,
    DetailStudyPlanDetailAPIView,
    DetailBankAccountAPIView,
    UserDataAPIView,
    ActiveCourseAPIView,
    SubscriptionAPIView,
    PaymentAPIView,
    SchoolAPIView,
)
from api.GenericsViews.GenericsListAPIView import (
    ListStudyPlanAPIView,
    ListUserByRoleAPIView,
    ListActiveCourseAPIView,
    ListSubscriptionAPIView,
    ListSchoolsAPIView,
    ListPersonalReferenceAPIView,
    ListUserBanksAccountsAPIView,
    ListStudentsByTeacherAPIView,
    listSchoolsByTeacherAPIView,
    ListActiveCoursesByUser,
    ListStudentsBySchoolTeacherAPIView,
)
from api.GenericsViews.GenericsCreateAPIViews import (
    CarateBanckAccountAPIView,
    CreateSchoolAPIView,
    CreateUserAPIView,
    CreatePersonalRefAPIView,
    CreateSubscriptionAPIView,
    CreatePaymentAPIView
)
from api.GenericsViews.GenericsDeleteAPIView import (
    DeleteBankAccountAPIView,
    DeleteSchoolAPIView,
    DeletePersonalRefAPIView,
)
from api.GenericsViews.GenericsUdpadeAPIViews import (
    UpdateBankAccountAPIView,
    UpdateSchoolAPIView,
    UpdateUserAPIView,
    UpdateUserPassword,
    UpdatePersonalRefAPIView,
    UpdatePaymentAPIView
)

from api.GenericsViews import (
    TeacherDataApiView,
    StudentDataAPIView,
    StudentDataForTeacherAPIView,
)

from api.GenericsViews import UploadCVFileView
from api.GenericsViews import UploadPictureFileAPIView

from api.accounts import LoginAPIView

from django.urls import path

app_name = "api"

urlpatterns = [
    # datos de usuario
    path(
        "user/update-password/<int:pk>/",
        UpdateUserPassword.as_view(),
        name="api-update-user-password",
    ),
    path(
        "user/upload-picture/<int:pk>/<str:type>/",
        UploadPictureFileAPIView.as_view(),
        name="api-upload-picture",
    ),
    path("user/update/<int:pk>/",
         UpdateUserAPIView.as_view(),
         name="api-update-user"
         ),
    path(
        "user/add/",
        CreateUserAPIView.as_view(),
        name="api-add-user"
    ),
    path(
        "user/<int:pk>/",
        UserDataAPIView.as_view(),
        name="api-user-data"
    ),
    path(
        "user/personal-reference/<int:pk>/",
        ListPersonalReferenceAPIView.as_view(),
        name="api-user-references"
    ),
    path(
        "user/banks-accounts/<int:id_user>/",
        ListUserBanksAccountsAPIView.as_view(),
        name="api-user-banks"
    ),
    path(
        "user/schools-by-teacher/<int:id_teacher>/",
        listSchoolsByTeacherAPIView.as_view(),
        name="api-schools-by-teacher"
    ),
    path(
        "user/students-by-teacher/<int:id_teacher>/",
        ListStudentsByTeacherAPIView.as_view(),
        name="api-students-by-teacher"
    ),
    path(
        "users-by-role/<str:role_name>/",
        ListUserByRoleAPIView.as_view(),
        name="api-users-by-role-list",
    ),
    path(
        "user/courses-by-user/<int:id_user>/",
        ListActiveCoursesByUser.as_view(),
        name="api-active-courses-by-user",
    ),
    path(
        "user/complete-data-teacher/<int:pk>/",
        TeacherDataApiView.as_view(),
        name="api-teacher-data",
    ),
    path(
        "user/complete-data-student/<int:pk>/",
        StudentDataAPIView.as_view(),
        name="api-student-data",
    ),
    path(
        "user/data-student-by-teacher/student/<int:id_student>/teacher/<int:id_teacher>/",
        StudentDataForTeacherAPIView.as_view(),
        name="api-student-data-teacher",
    ),
    path("user/upload-cv/<int:pk>/<str:filename>",
         UploadCVFileView.as_view(),
         name="api-upload-cv"
    ),
    path(
        'user/students-by-school-teacher/<int:id_user>/<int:id_school>/',
        ListStudentsBySchoolTeacherAPIView.as_view(),
        name="api-students-by-school-teacher",
    ),
    # bancos de usuario
    path(
        "bank-account/<int:pk>/",
        DetailBankAccountAPIView.as_view(),
        name="api-detail-bank-account",
    ),
    path(
        "bank-account/add/",
        CarateBanckAccountAPIView.as_view(),
        name="api-add-bank-account",
    ),
    path(
        "bank-account/delete/<int:pk>/",
        DeleteBankAccountAPIView.as_view(),
        name="api-delete-bank-account",
    ),
    path(
        "bank-account/update/<int:pk>/",
        UpdateBankAccountAPIView.as_view(),
        name="api-update-bank-account",
    ),
    # cursos activos
    path(
        "active-course/<int:pk>/",
        ActiveCourseAPIView.as_view(),
        name="api-active-course",
    ),
    path(
        "active-courses/",
        ListActiveCourseAPIView.as_view(),
        name="api-active-courses-list",
    ),
    # planes de estudio
    path(
        "study-plans/",
        ListStudyPlanAPIView.as_view(),
        name="api-list-study-plans"),
    path(
        "study-plan/<int:pk>/",
        DetailStudyPlanAPIView.as_view(),
        name="api-study-plan"
    ),
    path(
        "study-plan-detail/<int:pk>/",
        DetailStudyPlanDetailAPIView.as_view(),
        name="api-detail-study-plan",
    ),
    # suscripciones
    path(
        "subscription/<int:pk>/",
        SubscriptionAPIView.as_view(),
        name="api-subscription"
    ),
    path(
        "subscriptions/",
        ListSubscriptionAPIView.as_view(),
        name="api-subscriptions-list",
    ),
    path(
        "subscription/add/",
        CreateSubscriptionAPIView.as_view(),
        name="api-add-subscription",
    ),
    # pagos de suscripciones
    path(
        "payments-subscription/<int:pk>/",
        PaymentAPIView.as_view(),
        name="api-payments-subscription",
    ),
    path(
        "payment-subscription/add/",
        CreatePaymentAPIView.as_view(),
        name="api-add-payment",
    ),
    path(
        "payment-subscription/update/<int:pk>/",
        UpdatePaymentAPIView.as_view(),
        name="api-update-payment",
    ),
    # colegios
    path(
        "school/<int:pk>/",
        SchoolAPIView.as_view(),
        name="api-school-detail"
    ),
    path(
        "school/add/",
        CreateSchoolAPIView.as_view(),
        name="api-add-school"
    ),
    path(
        "school/delete/<int:pk>/",
        DeleteSchoolAPIView.as_view(),
        name="api-delete-school",
    ),
    path(
        "schools/",
        ListSchoolsAPIView.as_view(),
        name="api-schools-list"
    ),
    path(
        "school/update/<int:pk>/",
        UpdateSchoolAPIView.as_view(),
        name="api-update-school",
    ),
    # referencias personales
    path(
        "personal-reference/add/",
        CreatePersonalRefAPIView.as_view(),
        name="api-add-personal-reference",
    ),
    path(
        "personal-reference/delete/<int:pk>/",
        DeletePersonalRefAPIView.as_view(),
        name="api-delete-personal-reference",
    ),
    path(
        "personal-reference/update/<int:pk>/",
        UpdatePersonalRefAPIView.as_view(),
        name="api-update-personal-reference",
    ),
    # login
    path(
        "accounts/login/",
        LoginAPIView.as_view(),
        name="api-login",
    ),
]
