from os import environ, path
from pathlib import Path

from narrator import env

DJANGO_DEBUG = environ.get("DJANGO_DEBUG", True)
DEBUG = environ.get("DJANGO_DEBUG", True)

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "narrator.urls"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "narrator.apps.NarratorConfig",
    "rest_framework",
]

# Required to run admin panel
BASE_DIR = Path(__file__).resolve().parent.parent
DIRS = [str(BASE_DIR / "templates")]
CONTEXT_PROCESSORS = [
    "django.template.context_processors.request",
    "django.template.context_processors.debug",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.template.context_processors.request",
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": DIRS,
        "OPTIONS": {"context_processors": CONTEXT_PROCESSORS, "debug": DEBUG},
    },
]
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication"
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

STATIC_URL = "/static/"
STATIC_ROOT = path.join(BASE_DIR, "static")

SECRET_KEY = "secret"

SITE_ID = 1
LOGIN_URL = "/admin/login/"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": path.join(DATABASE_DIR, "narrator_local.db"),
#     },
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DJANGO_DB_NAME", "app"),
        "USER": env.str("DJANGO_DB_USER", "app"),
        "PORT": env.str("DJANGO_DB_PORT", "5432"),
        "PASSWORD": env.str("DJANGO_DB_PASSWORD", "app"),
        "HOST": env.str("DJANGO_DB_HOST", "localhost"),
        "ATOMIC_REQUESTS": True,
    }
}


# Redis Caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "narrator",
    }
}
# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15

RQ = {
    "DEFAULT_RESULT_TTL": 60_000,
}

RQ_QUEUES = {
    "default": {
        "USE_REDIS_CACHE": "default",
    },
    "high": {
        "USE_REDIS_CACHE": "default",
    },
    "low": {
        "USE_REDIS_CACHE": "default",
    },
}


LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    },
}

# Type of field to use for auto-created primary keys fields in Django models.
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = False

# AI - QDRANT - Vector Store
QDRANT_HOST = env.str("QDRANT_HOST", "localhost")
OLLAMA_HOST = env.str("OLLAMA_HOST", "localhost")
OLLAMA_PORT = env.int("OLLAMA_PORT", 11434)

###################################
# Debug mode configuration
if DEBUG:
    for queueConfig in RQ_QUEUES.values():
        queueConfig["ASYNC"] = "False"
