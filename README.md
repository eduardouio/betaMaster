Descripción del negocio:

Nuestro modelo se basa en ofrecer a la audiencia en general la posibilidad de acceder a la educación secundaria en el hogar permitiendoles continuar con sus estudios de manera segura y por el camino correcto,los estudiantes pueden postular al año escolar que le corresponda.Los aspirantes deben enviar sus documentos para inscribirse al colegio. Luego, el colegio revisa y aprueba o rechaza las solicitudes de los estudiantes. En caso de ser aprobados, los estudiantes proceden a pagar su matrícula y obtienen acceso al sistema, donde pueden seleccionar a un tutor de un catálogo que hemos preparado. Los estudiantes pueden elegir al profesor. La institución proporciona al profesor designado la estructura curricular y acceso al sistema Moodle para realizar el seguimiento y el registro del progreso del estudiante.

Documentos que los estudiantes deben cargar durante el proceso de inscripción:

    Cédula de Identidad
    Certificado del último año cursado
    Ciudad
    Dirección

Los profesores se postulan a través de la plataforma, cargan sus documentos y pasan por un proceso de validación por parte del colegio. Si son aprobados, se incluye en catálogo de profesores.

Documentos que los profesores deben proporcionar:

    Cédula de Identidad
    Título Universitario
    Certificado de Antecedentes
    Certificado de Salud
    Certificado de Trabajo
    Ciudad
    Dirección

El sistema debe gestionar:
    Un catálogo de profesores
    Un catálogo de estudiantes
    Un catálogo de cursos con sus materias (estructura curricular)
    El procesamiento de los pagos mensuales de los estudiantes
    El procesamiento de los pagos mensuales a los profesores
    La gestión de las inscripciones de nuevos estudiantes, con la opción de aceptar o rechazar las candidaturas
    La calificación de estudiantes, incluyendo el registro de sus documentos
    La calificación de profesores, también con el registro de sus documentos

Nuestro objetivo es facilitar el aprendizaje en el hogar, proporcionando a los estudiantes acceso a profesores cualificados y un entorno educativo estructurado a través de nuestra plataforma en línea.

-- sql para borrar el modeloo
DROP TABLE public.accounts_bankaccount CASCADE;
Z
DROP TABLE public.accounts_customusermodel CASCADE;
DROP TABLE public.accounts_customusermodel_groups CASCADE;
DROP TABLE public.accounts_customusermodel_user_permissions CASCADE;
DROP TABLE public.accounts_historicalbankaccount CASCADE;
DROP TABLE public.accounts_historicalpersonalreferences CASCADE;
DROP TABLE public.accounts_personalreferences CASCADE;
DROP TABLE public."activeCourses_activecourse" CASCADE;
DROP TABLE public."activeCourses_activecourse_teacher" CASCADE;
DROP TABLE public."activeCourses_historicalactivecourse" CASCADE;
DROP TABLE public.auth_group CASCADE;
DROP TABLE public.auth_group_permissions CASCADE;
DROP TABLE public.auth_permission CASCADE;
DROP TABLE public.django_admin_log CASCADE;
DROP TABLE public.django_content_type CASCADE;
DROP TABLE public.django_migrations CASCADE;
DROP TABLE public.django_session CASCADE;
DROP TABLE public.schools_historicalschool CASCADE;
DROP TABLE public.schools_school CASCADE;
DROP TABLE public."studyPlans_historicalstudyplan" CASCADE;
DROP TABLE public."studyPlans_historicalstudyplandetail" CASCADE;
DROP TABLE public."studyPlans_studyplan" CASCADE;
DROP TABLE public."studyPlans_studyplandetail" CASCADE;
DROP TABLE public.subscriptions_historicalpayment CASCADE;
DROP TABLE public.subscriptions_historicalsubscription CASCADE;
DROP TABLE public.subscriptions_payment CASCADE;
DROP TABLE public.subscriptions_subscription CASCADE;


Anotaciones de desarrollo
    Los colegios son administrados desde el admin de Django
    