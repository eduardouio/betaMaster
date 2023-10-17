LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MY_SECRET_KEY = 'HOME_SCHOOL_098765redcvbnmk0987654edvbnp98765dvbnk097654323457l,mnbvftyjdk@#$%^&*EVILLOTA'

app_database = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'home_schooling',
        'USER': 'eduardo',
        'PASSWORD': 'elian.2011',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    },
    'TEST': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE = app_database