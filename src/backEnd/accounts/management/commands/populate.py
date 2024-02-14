from dateutil.relativedelta import relativedelta
# importamos el comando par agenerar datos de prueba
from django.core.management.base import BaseCommand
# faker para los datos de prueba
from faker import Faker
import json
import random
# importamos los modelos
from accounts.models import CustomUserModel, PersonalReferences, BankAccount
from schools.models import School
from studyPlans.models import StudyPlan, StudyPlanDetail
from subscriptions.models import Subscription, Payment
from activeCourses.models import ActiveCourse

PRESENTATION = {
    'PROFESOR': '¡Hola! Soy un profesor con una carrera de 10 años en la educación. Mi pasión por enseñar y mi dedicación a fomentar el aprendizaje han sido los pilares de mi trayectoria profesional. A lo largo de los años, he tenido el privilegio de guiar a mis estudiantes hacia el éxito académico y personal. Mi enfoque pedagógico se centra en inspirar la curiosidad, fomentar el pensamiento crítico y proporcionar un ambiente de aprendizaje colaborativo. Estoy comprometido a crear un espacio educativo que motive a los estudiantes a alcanzar su máximo potencial.',
    'ESTUDIANTE': '¡Hola! Soy un estudiante apasionado y comprometido con mi educación en la escuela. Mi deseo de aprender y crecer me impulsa a aprovechar al máximo cada oportunidad académica. Me esfuerzo por destacar en mis estudios y participar activamente en el proceso educativo. Además, estoy abierto a nuevas experiencias y desafíos que me ayuden a desarrollar habilidades tanto dentro como fuera del aula. Estoy emocionado por el aprendizaje continuo y por contribuir positivamente al ambiente escolar.',
    'COLEGIO': '¡Bienvenidos a nuestra escuela! Somos una institución comprometida con la excelencia académica y el desarrollo integral de nuestros estudiantes. Nuestro equipo de educadores altamente calificados se esfuerza por proporcionar un ambiente de aprendizaje estimulante y enriquecedor. Valoramos la diversidad, la colaboración y el respeto mutuo. En nuestra escuela, nos esforzamos por inspirar el amor por el conocimiento, fomentar el crecimiento personal y preparar a nuestros estudiantes para enfrentar los desafíos del mundo con confianza y habilidades sólidas. ¡Estamos emocionados de tenerlos a bordo para este viaje educativo!',
    'COORDINADOR': 'Hola!, soy un coordinador, el rol de este usurio aun no esta claro, pero se que es importante.',
    'INVITADO': 'Hola!, soy un invitado, el rol de este usurio aun no esta claro, pero se que es importante.',
}


with open('accounts/management/commands/statesAndCitiesEC.json', 'r') as file:
    STATES_EC = json.load(file)

BANKS_NAME = [
    'Banco del Austro',
    'Banco de Guayaquil',
    'Banco de Machala',
    'Banco de Loja',
    'Banco de Pichincha',
    'Banco de la Producción',
    'Banco del Pacífico',
    'Banco Solidario',
    'Banco ProCredit',
    'Banco Internacional',
    'Banco Bolivariano',
    'Banco Amazonas',
    'Cooperativa de Ahorro y Crédito JEP',
    'Cooperativa de Ahorro y Crédito Policía Nacional',
    'Cooperativa de Ahorro y Crédito San Francisco',
    'Cooperativa de Ahorro y Crédito Santa Ana',
    'Cooperativa de Ahorro y Crédito 29 de Octubre',
    'Cooperativa de Ahorro y Crédito Alianza del Valle',
    'Cooperativa de Ahorro y Crédito CREA',
    'Cooperativa de Ahorro y Crédito CACPECO',
    'Cooperativa de Ahorro y Crédito ANDALUCIA',
]


class Command(BaseCommand):
    help = 'Comando para generar datos de prueba'

    def handle(self, *args, **kwargs):
        print('==>\tGenerando datos de prueba \n')
        fake = Faker('es_ES')
        print('Creando usuarios de prueba \n')
        self.create_users_by_profile(fake, 'ESTUDIANTE', 350)
        self.create_users_by_profile(fake, 'PROFESOR', 54)
        self.create_users_by_profile(fake, 'COORDINADOR', 12)
        self.create_users_by_profile(fake, 'COLEGIO', 27)
        self.create_users_by_profile(fake, 'INVITADO', 3)
        print('Registrando escuelas')
        self.create_schools(fake, 17)
        print('Registrando planes de estudio')
        self.create_stydu_plans(fake)
        for i in range(24):
            print('Registrando Cursos Activos')
            self.create_active_courses(fake)
        print('Registrando Subscripciones')
        self.create_subscriptions(fake)
        print('creando Bancos')
        self.create_user_banks(fake)
        print('creando Pagos')
        self.create_payments(fake)
        print('Referencias Personales')
        for i in range(15):
            if random.choice([False, False, True, False, True]):
                self.create_personal_references(fake)
        print('<==\t Datos de prueba generados')
        print('==>\t Definiendo roles con datos especifico')
        self.define_roles(fake)
        print('<==\t Roles definidos')
        print('==>\t cargado ultima sesion de los usuarios')
        self.load_last_sesion(fake)
        print('<==\t Ultima sesion cargada')

    def create_users_by_profile(self, fake, role, quantity):
        for i in range(quantity):
            ubication = fake.local_latlng(country_code='EC')
            my_state, my_citie, my_parroquia = self.select_city_and_parroquia()
            CustomUserModel.objects.create_user(
                email=str(random.randint(0, 10)) + '_' + fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_of_birth=fake.date_of_birth(),
                presentation=PRESENTATION[role],
                dni_number=fake.ssn(),
                address=fake.address(),
                url_instagram=random.choice([fake.url(), None]),
                url_facebook=random.choice([fake.url(), '']),
                url_twiter=random.choice([fake.url(), '']),
                url_linkedin=random.choice([fake.url(), '']),
                sex=random.choice(['hombre', 'mujer']),
                nationality=random.choice(
                    ['ECUATORIANO', 'COLOMBIANO', 'ECUATORIANO', 'PERUANO']
                ),
                is_aproved=random.choice([True, False, True]),
                have_disability=random.choice([False, False, True, False]),
                is_confirmed_mail=random.choice([True, False]),
                state=my_state,
                city=my_citie,
                parroquia=my_parroquia,
                phone=fake.phone_number(),
                civil_status=random.choice(
                    ['SOLTERO', 'CASADO', 'SOLTERO', 'DIVORCIADO', 'CASADO']
                ),
                geolocation=ubication[0] + ',' + ubication[1],
                password='1234.abc_',
                role=role,
            )

    def create_schools(self, fake, quantity):
        for i in range(quantity):
            my_state, my_citie, my_parroquia = self.select_city_and_parroquia()
            ubication = fake.local_latlng(country_code='EC')
            School.objects.create(
                name='Colegio ' + fake.company(),
                address=fake.address(),
                geolocation=ubication[0] + ',' + ubication[1],
                ami_code=fake.ssn(),
                state=my_state,
                city=my_citie,
                parroquia=my_parroquia,
                phone=fake.phone_number(),
                email=fake.company_email(),
                website=fake.url(),
                description=fake.text(),
                id_owner=CustomUserModel.objects.filter(
                    role='COLEGIO'
                ).order_by('?').first(),
                is_active=True,
                id_user_created=1,
                id_user_updated=1,
                url_facebook=fake.url(),
                url_linkedin=fake.url(),
                url_instagram=fake.url(),
                name_contact=fake.name(),
            )

    def create_stydu_plans(self, fake):
        name_plans = [
            'SÉPTIMO DE EDUCACIÓN GENERAL BÁSICA',
            'OCTAVO DE EDUCACIÓN GENERAL BÁSICA',
            'NOVENO DE EDUCACIÓN GENERAL BÁSICA',
            'DÉCIMO DE EDUCACIÓN GENERAL BÁSICA',
            'PRIMERO DE BACHILLERATO GENERAL UNIFICADO',
            'SEGUNDO DE BACHILLERATO GENERAL UNIFICADO',
            'TERCERO DE BACHILLERATO GENERAL UNIFICADO',
        ]
        for i in name_plans:
            user = CustomUserModel.objects.filter(
                role='COORDINADOR'
            ).order_by('?').first()

            StudyPlan.objects.create(
                name=i,
                coordinator=user,
                date_start=fake.past_datetime(),
                due_date=fake.future_datetime(),
                id_user_created=1,
                id_user_updated=1,
            )
        asignatures = [
            'CIENCIAS NATURALES',
            'CIENCIAS SOCIALES',
            'EDUCACIÓN ARTÍSTICA',
            'EDUCACIÓN ÉTICA Y VALORES',
            'EDUCACIÓN FÍSICA',
            'FÍSICA',
            'INGLÉS',
            'LENGUA Y LITERATURA',
            'MATEMÁTICAS',
            'QUIMICA'
            'TECNOLOGÍA',
        ]

        study_plans = StudyPlan.objects.all()
        for plan in study_plans:
            for i in asignatures:
                for level in range(3):
                    StudyPlanDetail.objects.create(
                        id_study_plan=plan,
                        asignature=i,
                        level=level,
                        credits=random.randint(15, 23),
                        minimun_score=7,
                        description=fake.paragraph(nb_sentences=4),
                        id_user_created=1,
                        id_user_updated=1,
                    )

    def create_active_courses(self, fake):
        all_schools = list(School.objects.all())
        all_teachers = list(CustomUserModel.objects.filter(role='PROFESOR'))
        all_students = list(CustomUserModel.objects.filter(role='ESTUDIANTE'))
        states = [
            'POR INICIAR',
            'EN PROCESO',
            'FINALIZADO',
        ]
        all_study_plans = StudyPlan.objects.all()
        for i, x in enumerate(states):
            for study_plan in all_study_plans:
                my_teacher = random.choice(all_teachers)
                active_course = ActiveCourse(
                    id_school=random.choice(all_schools),
                    id_study_plan=study_plan,
                    student=random.choice(all_students),
                    year=random.randint(2021, 2023),
                    state=x,
                    period=random.choice(
                        ['2021-2022', '2022-2023', '2022-2023']
                    ),
                    calification=random.randint(1, 10)
                )
                active_course.save()
                active_course.teacher.add(my_teacher)
                # agregamos un profesor adicional en algunos casos
                if random.choice([True, False, True, True]):
                    active_course.teacher.add(random.choice(all_teachers))
                if random.choice([True, False, False, False]):
                    active_course.teacher.add(random.choice(all_teachers))
                if random.choice([True, False, True, False]):
                    active_course.teacher.add(random.choice(all_teachers))
                active_course.save()

    def create_subscriptions(self, fake):
        all_users = CustomUserModel.objects.exclude(
            role='INVITADO'
        ).exclude(email='eduardouio7@gmail.com')
        active_courses = list(ActiveCourse.objects.all())
        for user in all_users:
            if random.choice([True, False, True, True]):
                my_cost = random.randint(21, 55)
                my_role = user.role.upper() if user.role.upper() != 'COORDINADOR' else 'OTRO'
                Subscription.objects.create(
                    id_user=user,
                    id_active_course=random.choice(active_courses),
                    date_start=fake.past_datetime(),
                    date_end=fake.future_datetime(),
                    type_subscription=my_role,
                    cost=round((my_cost/1.008), 2),
                    id_user_created=1,
                    id_user_updated=1,
                )

    def create_user_banks(self, fake):
        users = CustomUserModel.objects.exclude(role='GUEST').exclude(
            email='eduardouio7@gmail.com'
        )

        for x in range(10):
            for user in users:
                if random.choice([False, True, False, False]):
                    BankAccount.objects.create(
                        id_user=user,
                        nro_account=fake.aba(),
                        bank_name=random.choice(BANKS_NAME),
                        type_account=random.choice(['CORRIENTE', 'AHORROS']),
                        email_notify=fake.email(),
                        owner_name=' '.join([user.last_name, user.first_name]),
                        owner_dni=user.dni_number,
                    )

    def create_payments(self, fake):
        print('creando pagos')
        all_subscriptions = Subscription.objects.all()

        payment_status = [
            'PENDIENTE',
            'PAGADO',
            'ERROR',
            'DEVUELTO',
            'CANCELADO',
        ]
        for subscription in all_subscriptions:
            if random.choice([True, False, True, True]):
                user_bank = BankAccount.objects.filter(
                    id_user=subscription.id_user
                ).first()

                if user_bank is None:
                    break

                paymen_values = [
                    subscription.cost,
                    round(subscription.cost/1.05), 2,
                    round(subscription.cost/2.05), 2,
                    round(subscription.cost/3.05), 2,
                    round(subscription.cost/1.35), 2,
                ]
                Payment.objects.create(
                    id_subscription=subscription,
                    payment_date=fake.past_datetime(),
                    payment_amount=random.choice(paymen_values),
                    payment_status=random.choice(payment_status),
                    transaction_id=fake.bban(),
                    id_bank=user_bank,
                    account_destination=random.choice(['11111111', '222222']),
                    invoice_number=random.randint(100000, 999999),
                    id_user_created=1,
                    id_user_updated=1
                )

    def create_personal_references(self, fake):
        all_users = CustomUserModel.objects.filter(
            role='profesor'
        )
        start_date = fake.past_datetime()
        end_date = start_date + relativedelta(months=+random.randint(7, 38))
        for user in all_users:
            PersonalReferences.objects.create(
                id_user=user,
                type=random.choice(['PERSONAL', 'PROFESIONAL']),
                enterprise=fake.company(),
                name_contact=fake.name(),
                phone_contact=fake.phone_number(),
                email_contact=fake.email(),
                relationship=random.choice(
                    ['FAMILIAR', 'JEFE', 'AMIGO', 'OTRO']),
                is_verified=random.choice([True, False]),
                verification_date=fake.past_datetime(),
                start_date=start_date,
                end_date=end_date,
                verification_by=random.randint(1, 10),
            )

    def define_roles(self, fake):
        teachers = CustomUserModel.objects.filter(role='PROFESOR')
        for teacher in teachers:
            teacher.level_education = random.choice(
                ['DOCTORADO', 'SUPERIOR', 'MASTER', 'POSTGRADO', 'SUPERIOR']
            )
            teacher.save()

        students = CustomUserModel.objects.filter(have_disability=True)

        for student in students:
            student.disability_type = random.choice(
                ['VISUAL', 'AUDITIVA', 'MOTRIZ', 'INTELECTUAL', 'OTRA']
            )
            student.disability_persent = fake.random_int(min=1, max=100)
            student.card_conadis = fake.ssn()
            student.save()

    def load_last_sesion(self, fake):
        all_users = CustomUserModel.objects.exclude(
            role='INVITADO'
        ).exclude(email='eduardouio7@gmail.com')

        for user in all_users:
            user.last_login = fake.past_datetime()
            user.save()

    def select_city_and_parroquia(self):
        """
        Selecciona una ciudad y una parroquia de una provincia en especifico
        """
        my_state = random.choice([x for x in STATES_EC])
        my_city = random.choice([x for x in my_state['cantones']])
        my_parroquia = random.choice([x for x in my_city['parroquias']])
        return my_state['provincia'], my_city['canton'], my_parroquia
