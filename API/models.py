from django.db import models


class Client(models.Model):

    class Gender(models.TextChoices):
        MALE = "M", "male"
        FEMALE = "F", "female"
        OTHER = "O", "other"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=Gender.choices)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
