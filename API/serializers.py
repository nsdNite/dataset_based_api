from rest_framework import serializers

from API.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "category",
            "email",
            "gender",
            "birth_date",
        ]

        read_only_fields = ["id", "email"]
