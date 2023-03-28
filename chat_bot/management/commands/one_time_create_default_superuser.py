from os import getenv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

DEFAULT_SUPERUSER_FIRSTNAME = getenv("DEFAULT_SUPERUSER_FIRSTNAME")
DEFAULT_SUPERUSER_LASTNAME = getenv("DEFAULT_SUPERUSER_LASTNAME")
DEFAULT_SUPERUSER_EMAIL = getenv("DEFAULT_SUPERUSER_EMAIL")
DEFAULT_SUPERUSER_USERNAME = getenv("DEFAULT_SUPERUSER_USERNAME")
DEFAULT_SUPERUSER_PASSWORD = getenv("DEFAULT_SUPERUSER_PASSWORD")


class Command(BaseCommand):
    help = "Creates default Super User instance"

    def handle(self, *args, **options):
        User.objects.get_or_create(
            username=DEFAULT_SUPERUSER_USERNAME,
            defaults={
                "first_name": DEFAULT_SUPERUSER_FIRSTNAME,
                "last_name": DEFAULT_SUPERUSER_LASTNAME,
                "email": DEFAULT_SUPERUSER_EMAIL,
                "password": make_password(DEFAULT_SUPERUSER_PASSWORD),
                "is_superuser": True,
                "is_staff": True,
            },
        )
