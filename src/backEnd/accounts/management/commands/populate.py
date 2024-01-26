# importamos el comando par agenerar datos de prueba
from django.core.management.base import BaseCommand
# faker para los datos de prueba
from faker import Faker
import random
# importamos los modelos
from accounts.models import CustomUserModel, PersonalReferences, BankAccount
from schools.models import School
from studyPlans.models import StudyPlan, StudyPlanDetail
from subscriptions.models import Subscription, Payment
from activeCourses.models import ActiveCourse

PRESNTATION = {
    'teacher': '¡Hola! Soy un profesor con una carrera de 10 años en la educación. Mi pasión por enseñar y mi dedicación a fomentar el aprendizaje han sido los pilares de mi trayectoria profesional. A lo largo de los años, he tenido el privilegio de guiar a mis estudiantes hacia el éxito académico y personal. Mi enfoque pedagógico se centra en inspirar la curiosidad, fomentar el pensamiento crítico y proporcionar un ambiente de aprendizaje colaborativo. Estoy comprometido a crear un espacio educativo que motive a los estudiantes a alcanzar su máximo potencial.',
    'student': '¡Hola! Soy un estudiante apasionado y comprometido con mi educación en la escuela. Mi deseo de aprender y crecer me impulsa a aprovechar al máximo cada oportunidad académica. Me esfuerzo por destacar en mis estudios y participar activamente en el proceso educativo. Además, estoy abierto a nuevas experiencias y desafíos que me ayuden a desarrollar habilidades tanto dentro como fuera del aula. Estoy emocionado por el aprendizaje continuo y por contribuir positivamente al ambiente escolar.',
    'school': '¡Bienvenidos a nuestra escuela! Somos una institución comprometida con la excelencia académica y el desarrollo integral de nuestros estudiantes. Nuestro equipo de educadores altamente calificados se esfuerza por proporcionar un ambiente de aprendizaje estimulante y enriquecedor. Valoramos la diversidad, la colaboración y el respeto mutuo. En nuestra escuela, nos esforzamos por inspirar el amor por el conocimiento, fomentar el crecimiento personal y preparar a nuestros estudiantes para enfrentar los desafíos del mundo con confianza y habilidades sólidas. ¡Estamos emocionados de tenerlos a bordo para este viaje educativo!',
    'coordinator': 'Hola!, soy un coordinador, el rol de este usurio aun no esta claro, pero se que es importante.',
    'guest': 'Hola!, soy un invitado, el rol de este usurio aun no esta claro, pero se que es importante.',
}


STATES_EC = {
    "Azuay": [
        "Cuenca", "Gualaceo", "Paute", "Santa Isabel", "Sigsig",
        "Chordeleg", "Girón", "Nabón", "Oña", "Pucará", "San Fernando",
        "Sevilla de Oro", "Sígsig", "El Pan", "Tarqui",
    ],
    "Bolívar": [
        "Guaranda", "Caluma", "Chillanes", "San Miguel", "Las Naves",
        "Echeandía", "San José de Chimbo", "Las Mercedes",
        "Salinas", "Balsapamba",
    ],
    "Cañar": [
        "Azogues", "Biblián", "La Troncal", "Déleg", "Tambo", "Suscal",
        "El Tambo", "Zhud", "El Corazón", "Canaribamba"
    ],
    "Carchi": [
        "Tulcán", "Montúfar", "Mira", "Bolívar", "San Gabriel",
        "Huaca", "El Ángel", "Julio Andrade", "Tufiño", "Chical",
    ],
    "Chimborazo": [
        "Riobamba", "Alausí", "Colta", "Guamote", "Pallatanga",
        "Chunchi", "Cumandá", "Guano", "Penipe", "Chambo",
    ],
    "Cotopaxi": [
        "Latacunga", "Saquisilí", "Salcedo", "Pujilí", "La Maná",
        "Sigchos", "San Miguel de Salcedo", "Tanicuchí", "Toacaso",
        "Mulaló"
    ],
    "El Oro": [
        "Machala", "Pasaje", "Santa Rosa", "Huaquillas", "El Guabo",
        "Piñas", "Zaruma", "Atahualpa", "Balsas", "Marcabelí",
    ],
    "Esmeraldas": [
        "Esmeraldas", "Atacames", "Muisne", "Tonsupa", "Quinindé",
        "La Concordia", "San Lorenzo", "Río Verde", "Limones",
        "Chamanga",
    ],
    "Galápagos": [
        "Isabela (o Isla Isabela)", "Santa Cruz (o Isla Santa Cruz)",
        "San Cristóbal (o Isla San Cristóbal)",
        "Floreana (o Isla Floreana)", "Baltra (o Isla Baltra)",
        "Santiago (o Isla Santiago)", "Fernandina (o Isla Fernandina)",
        "Española (o Isla Española)", "Genovesa (o Isla Genovesa)",
        "Santa Fe (o Isla Santa Fe)",
    ],
    "Guayas": [
        "Guayaquil", "Daule", "Durán", "Samborondón", "Milagro",
        "Naranjal", "Playas", "Salitre", "Yaguachi", "El Triunfo",
    ],
    "Imbabura": [
        "Ibarra", "Otavalo", "Cotacachi", "Atuntaqui", "Pimampiro",
        "Urcuquí", "San Antonio de Ibarra", "San Miguel de Urcuquí",
        "Salinas", "La Esperanza"
    ],
    "Loja": [
        "Loja", "Catacocha", "Macará", "Zapotillo", "Cariamanga",
                "Quilanga", "Chaguarpamba", "Pindal", "Espíndola", "Sozoranga"
    ],
    "Los Ríos": [
        "Babahoyo", "Quevedo", "Ventanas", "Vinces", "Puebloviejo",
        "Valencia", "Urdaneta", "Buena Fé", "Mocache", "Quevedo"
    ],
    "Manabí": [
        "Portoviejo", "Manta", "Montecristi", "Jipijapa", "Chone",
        "El Carmen", "Rocafuerte", "24 de Mayo", "Santa Ana", "Calceta"
    ],
    "Morona Santiago": [
        "Macas", "Gualaquiza", "Sucúa", "Limon", "Morona", "Logroño",
        "Pablo Sexto", "Taisha", "Palora", "San Juan Bosco"
    ],
    "Napo": [
        "Tena", "El Chaco", "Quijos", "Archidona",
                "Carlos Julio Arosemena Tola", "El Chaco", "Quijos", "Talag",
                "El Juncal", "Baeza"
    ],
    "Orellana": [
        "Orellana", "La Joya de los Sachas", "Lago Agrio",
        "Shushufindi", "Aguarico", "Santa Rosa", "Coca",
        "Joyas de los Sachas", "San Carlos"
    ],
    "Pastaza": [
        "Puyo", "Santa Clara", "Arajuno", "Mera", "Shell", "Naranjal",
                "Pomona", "Río Corrientes", "Río Tigre", "Canelos"
    ],
    "Pichincha": [
        "Quito", "Sangolquí", "Cayambe", "Machachi", "Mejía",
        "Pedro Moncayo", "Puerto Quito", "Rumiñahui",
        "San Miguel de Los Bancos", "Pedro Vicente Maldonado"
    ],
    "Santa Elena": [
        "Santa Elena", "Salinas", "La Libertad", "La Libertad",
        "Salinas", "Santa Elena", "Ballenita", "Atahualpa", "Anconcito",
        "Anconcito"
    ],
    "Santo Domingo de los Tsáchilas": [
        "Santo Domingo", "La Concordia", "La Concordia",
        "La Independencia", "Valle Hermoso", "Valle Hermoso",
        "San Jacinto del Búa", "El Carmen", "El Carmen", "Alluriquín"
    ],
    "Sucumbíos": [
        "Nueva Loja", "Shushufindi", "Lumbaquí", "Gonzalo Pizarro",
        "Putumayo", "Cuyabeno", "Cascales", "Agua Blanca",
        "Sucumbíos", "Tarapoa"
    ],
    "Tungurahua": [
        "Ambato", "Banos", "Pelileo", "Patate", "Mocha", "Cevallos",
        "Quero", "Pillaro", "Tisaleo", "Baños de Agua Santa"
    ],
    "Zamora Chinchipe": [
        "Zamora", "Yantzaza", "Zamora", "Yantzaza", "Zumbi",
        "Centinela del Cóndor", "Palanda", "Nangaritza", "Yacuambi",
        "El Pangui"
    ]
}

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
        self.create_users_by_profile(fake, 'student', 250)
        self.create_users_by_profile(fake, 'teacher', 74)
        self.create_users_by_profile(fake, 'coordinator', 12)
        self.create_users_by_profile(fake, 'school', 27)
        self.create_users_by_profile(fake, 'guest', 18)
        print('Registrando escuelas')
        self.create_schools(fake, 27)
        print('Registrando planes de estudio')
        self.create_stydu_plans(fake)
        for i in range(10):
            print('Registrando Cursos Activos')
            self.create_active_courses(fake)
        print('Registrando Subscripciones')
        self.create_subscriptions(fake)
        print('creando Bancos')
        self.create_user_banks(fake)
        print('creando Pagos')
        self.create_payments(fake)
        print('Referencias Personales')
        self.create_personal_references(fake)
        print('<==\t Datos de prueba generados')
        print('==>\t Definiendo roles con datos especifico')
        self.define_roles(fake)
        print('<==\t Roles definidos')

    def create_users_by_profile(self, fake, role, quantity):
        for i in range(quantity):
            my_state = random.choice(list(STATES_EC.keys()))
            CustomUserModel.objects.create_user(
                email=str(random.randint(0, 10)) + '_' + fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_of_birth=fake.date_of_birth(),
                presentation=PRESNTATION[role],
                dni_number=fake.ssn(),
                address=fake.address(),
                url_instagram=random.choice([fake.url(), None]),
                url_facebook=random.choice([fake.url(), '']),
                url_twiter=random.choice([fake.url(), '']),
                url_linkedin=random.choice([fake.url(), '']),
                sex=random.choice(['male', 'female']),
                nationality=random.choice(
                    ['ECUATORIANO', 'COLOMBIANO', 'ECUATORIANO', 'PERUANO']
                ),
                is_aproved=random.choice([True, False, True]),
                have_disability=random.choice([False, False, True, False]),
                is_confirmed_mail=random.choice([True, False]),
                state=my_state,
                city=random.choice(STATES_EC[my_state]),
                civil_status=random.choice(
                    ['single', 'married', 'free_union', 'divorced', 'single']
                ),
                geolocation=fake.local_latlng(country_code='EC'),
                password='1234.abc_',
                role=role,
            )

    def create_schools(self, fake, quantity):
        for i in range(quantity):
            my_state = random.choice(list(STATES_EC.keys()))
            School.objects.create(
                name='Colegio  ' + fake.company(),
                address=fake.address(),
                geolocation=fake.local_latlng(country_code='EC'),
                ami_code=fake.ssn(),
                state=my_state,
                city=random.choice(STATES_EC[my_state]),
                phone=fake.phone_number(),
                email=fake.company_email(),
                website=fake.url(),
                description=fake.text(),
                id_owner=CustomUserModel.objects.filter(
                    role='school'
                ).order_by('?').first(),
                is_active=True,
                id_user_created=1,
                id_user_updated=1,
            )

    def create_stydu_plans(self, fake):
        name_plans = [
            'Séptimo de Educación General Básica',
            'Octavo de Educación General Básica',
            'Noveno de Educación General Básica',
            'Décimo de Educación General Básica',
            'Primero de Bachillerato General Unificado',
            'Segundo de Bachillerato General Unificado',
            'Tercero de Bachillerato General Unificado',
        ]
        for i in name_plans:
            user = CustomUserModel.objects.filter(
                role='coordinator'
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
            'Ciencias Naturales',
            'Ciencias Sociales',
            'Educación Artística',
            'Educación Ética y Valores',
            'Educación Física',
            'Física',
            'Inglés',
            'Lengua y Literatura',
            'Matemáticas',
            'Quimica'
            'Tecnología',
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
        all_teachers = list(CustomUserModel.objects.filter(role='teacher'))
        all_students = list(CustomUserModel.objects.filter(role='student'))
        states = [
            'POR INICIAR',
            'EN PROCESO',
            'FINALIZADO',
        ]
        all_study_plans = StudyPlan.objects.all()
        for i in range(7):
            for study_plan in all_study_plans:
                my_teacher = random.choice(all_teachers)
                active_course = ActiveCourse(
                    id_school=random.choice(all_schools),
                    id_study_plan=study_plan,
                    student=random.choice(all_students),
                    year=random.randint(2021, 2023),
                    state=random.choice(states),
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
            role='guest'
        ).exclude(email='eduardouio7@gmail.com')
        active_courses = list(ActiveCourse.objects.all())
        for user in all_users:
            if random.choice([True, False, True, True]):
                my_cost = random.randint(21, 55)
                my_role = user.role.upper() if user.role.upper() != 'cordinator' else 'OTHER'
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
        users = CustomUserModel.objects.exclude(role='guest').exclude(
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
            'PENDING',
            'PAID',
            'FAILED',
            'REFUNDED',
            'CANCELLED',
            'EXPIRED',
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
            role='teacher'
        )
        for user in all_users:
            PersonalReferences.objects.create(
                id_user=user,
                type=random.choice(['personal', 'professional']),
                enterprise=fake.company(),
                name_contact=fake.name(),
                phone_contact=fake.phone_number(),
                email_contact=fake.email(),
                relationship=random.choice(
                    ['family', 'boss', 'buddy', 'other']),
                is_verified=random.choice([True, False]),
                verification_date=fake.past_datetime(),
                verification_by=random.randint(1, 10),
            )

    def define_roles(self, fake):
        teachers = CustomUserModel.objects.filter(role='teacher')
        for teacher in teachers:
            teacher.level_education = random.choice(
                ['doctorado', 'superior', 'master', 'postgrado', 'superior']
            )
            teacher.save()

        students = CustomUserModel.objects.filter(have_disability=True)

        for student in students:
            student.disability_type = random.choice(
                ['visual', 'auditiva', 'motriz', 'intelectual', 'otra']
            )
            student.disability_persent = fake.random_int(min=1, max=100)
            student.card_conadis = fake.ssn()
            student.save()
