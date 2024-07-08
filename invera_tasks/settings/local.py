from invera_tasks.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("PGSQL_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.environ.get("PGSQL_DATABASE", os.path.join(BASE_DIR, "testdb")),
        "USER": os.environ.get("PGSQL_USER", "admin"),
        "PASSWORD": os.environ.get("PGSQL_PASSWORD", "admin"),
        "HOST": os.environ.get("PGSQL_HOST", "127.0.0.1"),
        "PORT": os.environ.get("PGSQL_PORT", 5432)
    }
}