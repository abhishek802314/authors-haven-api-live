from .base import *
from .base import env


DEBUG = True


SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-9ek&*lag6))g5$+l16ke)pbj6pwkp9!p7%q9#xpqnn=2y$6ivg")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]