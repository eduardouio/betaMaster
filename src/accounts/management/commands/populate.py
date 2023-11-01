# importamos el comando par agenerar datos de prueba
from django.core.management.base import BaseCommand
# faker para los datos de prueba
from faker import Faker
import random
# importamos los modelos
from accounts.models import CustomUserModel
from schools.models import School
from studyPlans.models import StudyPlan, StudyPlanDetail
from subscriptions.models import Subscription, Payment
from activeCourses.models import ActiveCourse
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


class Command(BaseCommand):
    help = 'Comando para generar datos de prueba'

    def handle(self, *args, **kwargs):
        print('==>\tGenerando datos de prueba \n')
        fake = Faker('es_ES')
        # print('Creando usuarios de prueba \n')
        # self.create_users_by_profile(fake, 'student', 150)
        # self.create_users_by_profile(fake, 'teacher', 54)
        # self.create_users_by_profile(fake, 'coordinator', 10)
        # self.create_users_by_profile(fake, 'school', 27)
        # self.create_users_by_profile(fake, 'guest', 3)
        # print('RRegistrando escuelas')
        # self.create_schools(fake, 27)
        # print('Registrando planes de estudio')
        # self.create_stydu_plans(fake)
        # print('Registrando Cursos Activos')
        self.create_active_courses(fake)
        print('Registrando Subscripciones')
        self.create_subscriptions(fake)
        print('Pagos')
        self.create_payments(fake)
        print('<==\t Datos de prueba generados')

    def create_users_by_profile(self, fake, role, quantity):
        for i in range(quantity):
            my_state = random.choice(list(STATES_EC.keys()))
            CustomUserModel.objects.create_user(
                username=fake.user_name() + str(random.randint(0, 10)),
                email=str(random.randint(0, 10)) + fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_of_birth=fake.date_of_birth(),
                dni_number=fake.ssn(),
                address=fake.address(),
                is_aproved=True,
                state=my_state,
                city=random.choice(STATES_EC[my_state]),
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
                dni_collegue=fake.ssn(),
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
                ActiveCourse.objects.create(
                    id_school=random.choice(all_schools),
                    id_study_plan=study_plan,
                    id_teacher=my_teacher.pk,
                    id_student=random.choice(all_students),
                    year=random.randint(2021, 2023),
                    state=random.choice(states),
                    period=random.choice(
                        ['2021-2022', '2022-2023', '2022-2023']
                    ),
                    calification=random.randint(1, 10),
                )

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

    def create_payments(self, fake):
        all_subscriptions = Subscription.objects.all()
        all_banks = [
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
        payment_status = [
            'PENDING',
            'PAID',
            'FAILED',
            'REFUNDED',
            'CANCELLED',
            'EXPIRED',
        ]
        if random.choice([True, False, True]):
            for subscription in all_subscriptions:
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
                    bank_name=random.choice(all_banks),
                    owner_account=fake.iban(),
                    dni_owner_account=fake.ssn(),
                    account_number=fake.aba(),
                    account_destination=random.choice(['11111111', '222222']),
                    invoice_number=random.randint(100000, 999999),
                    id_user_created=1,
                    id_user_updated=1
                )
