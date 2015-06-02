import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={"default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    }}
)
try:
    django.setup()
except AttributeError:
    from django.core.management import setup_environ
    setup_environ(settings)
