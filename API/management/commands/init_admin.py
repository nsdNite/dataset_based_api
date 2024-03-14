import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = os.getenv("ADMIN_USRENAME")
            password = os.getenv("ADMIN_PASSWORD")
            print("Creating superuser")
            User.objects.create_superuser(username=username, password=password)
        else:
            print(
                "Admin accounts can only be initialized if no Accounts exist"
            )
