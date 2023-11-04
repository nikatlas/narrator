from os import environ, path

from narrator.constants import DATABASE_DIR

DEBUG = environ.get("DJANGO_DEBUG", False)
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = ["narrator.apps.NarratorConfig"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": path.join(DATABASE_DIR, "narrator_local.db"),
    },
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

###################################
# Debug mode configuration
if DEBUG:
    for queueConfig in RQ_QUEUES.values():
        queueConfig["ASYNC"] = "False"
