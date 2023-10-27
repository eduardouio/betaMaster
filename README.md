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
DROP TABLE public.accounts_customusermodel;
DROP TABLE public.accounts_customusermodel_groups;
DROP TABLE public.accounts_customusermodel_user_permissions;
DROP TABLE public."activeCourses_activecourse";
DROP TABLE public."activeCourses_historicalactivecourse";
DROP TABLE public.auth_group;
DROP TABLE public.auth_group_permissions;
DROP TABLE public.auth_permission;
DROP TABLE public.django_admin_log;
DROP TABLE public.django_content_type;
DROP TABLE public.django_migrations;
DROP TABLE public.django_session;
DROP TABLE public.schools_historicalschool;
DROP TABLE public.schools_school;
DROP TABLE public."studyPlans_historicalstudyplan";
DROP TABLE public."studyPlans_historicalstudyplandetail";
DROP TABLE public."studyPlans_studyplan";
DROP TABLE public."studyPlans_studyplandetail";
DROP TABLE public.subscriptions_historicalpayment;
DROP TABLE public.subscriptions_historicalsubscription;
DROP TABLE public.subscriptions_payment;
DROP TABLE public.subscriptions_subscription;
