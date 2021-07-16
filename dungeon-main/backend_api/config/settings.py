import os

import environ

env = environ.Env()

BASE_DIR = environ.Path(__file__) - 2


ROOT_DIR = BASE_DIR - 1
env.read_env(str(ROOT_DIR.path("envs/.env")))


SECRET_KEY = env.str("SECRET_KEY")


DEBUG = env.bool("DEBUG", default=True)


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    'rest_framework.authtoken',
    'drf_yasg',
    'graphene_django',

    # when celery-beat will stop supporting Django < 2 we can swap this:
    "django_celery_beat.apps.BeatConfig",
    # to this:
    # "django_celery_beat",
    # i just don't want to see warnings in pytest associated with fucking default_app_config
]

LOCAL_APPS = [
    'inventories.apps.InventoriesConfig',
    'paths.apps.PathsConfig',
    'users.apps.UsersConfig',
    'textures.apps.TexturesConfig',
    'dungeons.apps.DungeonsConfig',
    'monsters.apps.MonstersConfig',
    'questions.apps.QuestionsConfig',
    'chat.apps.ChatConfig',
    'invitations.apps.InvitationsConfig',
    'rooms.apps.RoomsConfig',
    'floors.apps.FloorsConfig',
    'levels.apps.LevelsConfig',
    'spells.apps.SpellsConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "users.middleware.last_user_activity_middleware"
]

LAST_ACTIVITY_INTERVAL = 86400

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": env.db("DATABASE_URL"),
    "mongodb": {
        'ENGINE': 'djongo',
        'NAME': env.str('MONGO_INITDB_DATABASE'),
        "CLIENT": {
            "host": env.str("MONGO_HOST"),
            "username": env.str("MONGO_INITDB_ROOT_USERNAME"),
            "password": env.str("MONGO_INITDB_ROOT_PASSWORD"),
            "port": env.int("MONGODB_PORT"),
            "authSource": env.str("AUTH_SOURCE"),
            "authMechanism": env.str("AUTH_MECHANISM")
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = env("REDIS_URL")

CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'common.utils.custom_exc_handler',
    'DEFAULT_THROTTLE_RATES': {
        'friend-request': '10/min',
        'create-user': '5/min'
    },
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ]
}
