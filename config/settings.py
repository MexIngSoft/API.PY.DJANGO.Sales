from pathlib import Path
import dotenv
import dj_database_url
import sys
from os import getenv, path

# ===============================
# PROJECT INFO
# ===============================
PROJECT_NAME = "Sales"
DB_SCHEMA = getenv("DB_SCHEMA", PROJECT_NAME)

# ===============================
# BASE
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = BASE_DIR / ".env.local"

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

DEVELOPMENT_MODE = getenv("DEVELOPMENT_MODE", "False") == "True"

# ===============================
# CORE DJANGO
# ===============================
SECRET_KEY = getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("DJANGO_SECRET_KEY no definido")

ALLOWED_HOSTS = getenv(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

DEBUG = DEVELOPMENT_MODE

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
            ],
        },
    },
]

# ===============================
# APPLICATIONS
# ===============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",

    # Apps propias (ejemplos)
    "sales",
]

# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# ===============================
# DATABASE
# ===============================
if DEVELOPMENT_MODE:

    DATABASES = {
        "default": {
            "ENGINE": getenv("DB_ENGINE", "django.db.backends.postgresql"),
            "NAME": getenv("POSTGRES_DB"),
            "USER": getenv("POSTGRES_USER"),
            "PASSWORD": getenv("POSTGRES_PASSWORD"),
            "HOST": getenv("POSTGRES_HOST", "localhost"),
            "PORT": getenv("POSTGRES_PORT", "5432"),
            "OPTIONS": {
                "options": f"-c search_path=\"{DB_SCHEMA}\",public"
            },
        }
    }

elif len(sys.argv) > 0 and sys.argv[1] != "collectstatic":

    if getenv("DATABASE_URL") is None:
        raise Exception("DATABASE_URL environment variable not defined")

    DATABASES = {
        "default": dj_database_url.parse(getenv("DATABASE_URL"))
    }

# ===============================
# REST
# ===============================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

AUTH_API_VERIFY_URL = getenv("AUTH_API_VERIFY_URL", "http://api-backend-python:8000/api/auth/jwt/verify/")

# ===============================
# CORS
# ===============================
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = getenv(
    "CORS_ALLOWED_ORIGINS",
    "http://localhost:3000"
).split(",")

# ===============================
# STATIC / MEDIA
# ===============================
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

if DEVELOPMENT_MODE:
    STATIC_ROOT = BASE_DIR / "static"
    MEDIA_ROOT = BASE_DIR / "media"

# ===============================
# I18N
# ===============================
LANGUAGE_CODE = "es-mx"
TIME_ZONE = "America/Mexico_City"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
