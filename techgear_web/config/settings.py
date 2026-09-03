"""
Django settings for config project.
"""

import os
from pathlib import Path


# ---------------------------------------------------------
# Rutas
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# Seguridad
# ---------------------------------------------------------

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-%l8$*8-(plm#kv*$3d_p73vl8wycmwe@v-@x#s465kg0j6%0%b"
)

DEBUG = False


# ---------------------------------------------------------
# Hosts permitidos
# ---------------------------------------------------------

VERCEL_URL = os.getenv("VERCEL_URL")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "tech-gear-22iusx4oh-breiner200718.vercel.app",
]
if VERCEL_URL:
    ALLOWED_HOSTS.append(VERCEL_URL)


# ---------------------------------------------------------
# CSRF
# ---------------------------------------------------------

CSRF_TRUSTED_ORIGINS = [
    "https://tech-gear-22iusx4oh-breiner200718.vercel.app",
]

if VERCEL_URL:
    ALLOWED_HOSTS.append(VERCEL_URL)

if VERCEL_URL:
    CSRF_TRUSTED_ORIGINS.append(
        f"https://{VERCEL_URL}"
    )


# ---------------------------------------------------------
# Aplicaciones
# ---------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "techgear",
]


# ---------------------------------------------------------
# Middleware
# ---------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ---------------------------------------------------------
# URLs
# ---------------------------------------------------------

ROOT_URLCONF = "config.urls"


# ---------------------------------------------------------
# Templates
# ---------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "techgear" / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ---------------------------------------------------------
# WSGI
# ---------------------------------------------------------

WSGI_APPLICATION = "config.wsgi.application"


# ---------------------------------------------------------
# Base de datos
# ---------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------
# Validación de contraseñas
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Internacionalización
# ---------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ---------------------------------------------------------
# Archivos estáticos
# ---------------------------------------------------------

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# ---------------------------------------------------------
# Email
# ---------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"