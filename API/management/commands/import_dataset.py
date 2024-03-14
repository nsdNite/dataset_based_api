import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from tqdm import tqdm

from API.models import Client


class Command(BaseCommand):
    """Loads a CSV file into a database"""

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str)

    def handle(self, *args, **options):
        with open(options["filename"]) as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in tqdm(csv_reader, desc="Loading database:"):
                gender_mapping = {
                    "male": Client.Gender.MALE,
                    "female": Client.Gender.FEMALE,
                    "other": Client.Gender.OTHER,
                }
                gender = gender_mapping.get(
                    row["gender"].lower(), Client.Gender.OTHER
                )

                birth_date = datetime.strptime(
                    row["birthDate"], "%Y-%m-%d"
                ).date()

                Client.objects.update_or_create(
                    email=row["email"],
                    defaults={
                        "first_name": row["firstname"],
                        "last_name": row["lastname"],
                        "gender": gender,
                        "birth_date": birth_date,
                    },
                )
