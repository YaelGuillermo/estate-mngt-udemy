from os import getenv, path

from dotenv import load_dotenv

from .base import * # noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

DEBUG = True

SITE_NAME = getenv("SITE_NAME")

SECRET_KEY = getenv("DJANGO_SECRET_KEY", "-3qlUIk9xgEqq21q40R05KhJsfPkIGAEw9dMsp5fOl-vSyv2CWA")

#"django-insecure-sl!j^tdz4o9u=okix_fh+dzpaz&fz&m-+5=v@kk+-5foy8^+9d"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

ADMIN_URL = getenv("DJANGO_ADMIN_URL")
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER")
DOMAIN = getenv("DOMAIN")

LOGGING = {
    "version": 1, 
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s [%(name)-12s] %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": { 
        "handlers": ["console"],
        "level": "INFO",
    },
}