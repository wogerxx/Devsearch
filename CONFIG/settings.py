import os
from pathlib import Path
from environs import Env
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "MAIN.apps.MainConfig",
    "USERS.apps.UsersConfig",

    # social Oauth
    'social_django'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    #i18n tillar uchun middlewhere
    "django.middleware.locale.LocaleMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # social Oauth
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = "CONFIG.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # social Oauth
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = "CONFIG.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER':env.str('DB_USER'),
        'PASSWORD':env.str('DB_PASSWORD'),
        'PORT': env.int('DB_PORT'),
        'HOST':env.str('DB_HOST'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("uz", _("Uzbek")),
    ("ru", _("Russian")),
]

LOCALE_PATHS = [BASE_DIR/'locale']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR/'staticfiles']
STATIC_ROOT = BASE_DIR/'static'

MEDIA_URL ='media/'
MEDIA_ROOT = BASE_DIR/'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = 'USERS.User'

# Foydalanuvchi muvaffaqiyatli tizimga kirgandan so'ng yo'naltiriladigan sahifa
LOGIN_REDIRECT_URL = reverse_lazy('developers')

# Foydalanuvchi tizimdan chiqqandan so'ng yo'naltiriladigan sahifa
LOGOUT_REDIRECT_URL = reverse_lazy('login')


AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env.str("GOOGLE_KEY_USER")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env.str("GOOGLE_KEY_SECRET")



SOCIAL_AUTH_GITHUB_KEY = env.str("GIT_KEY_USER")
SOCIAL_AUTH_GITHUB_SECRET = env.str("GIT_KEY_SECRET")

SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://127.0.0.1:8000/en/'



# email configs

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env.str('EMAIL_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_PASSWORD')
