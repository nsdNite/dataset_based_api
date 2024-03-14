from datetime import date, timedelta

from rest_framework import viewsets, status
from rest_framework.response import Response

from API.models import Client
from API.serializers import ClientSerializer
from API.pagination import ClientPagination


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientPagination

    def get_queryset(self):
        category = self.request.query_params.get("category", None)
        gender = self.request.query_params.get("gender", None)
        birth_date = self.request.query_params.get("birth_date", None)
        age = self.request.query_params.get("age", None)
        age_min = self.request.query_params.get("age_min", None)
        age_max = self.request.query_params.get("age_max", None)
        queryset = self.queryset

        if category:
            queryset = queryset.filter(category=category)

        if gender:
            queryset = queryset.filter(gender=gender)

        if birth_date:
            queryset = queryset.filter(birth_date=birth_date)

        if age:
            try:
                age = int(age)
                now = date.today()
                birthdate_from = now - timedelta(days=(age + 1) * 365)
                birthdate_to = now - timedelta(days=age * 365)
                queryset = queryset.filter(
                    birthDate__range=[birthdate_from, birthdate_to]
                )
            except ValueError:
                return Response(
                    {"error": "Invalid age value provided."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if age_min and age_max:
            try:
                age_min = int(age_min)
                age_max = int(age_max)
                now = date.today()
                birthdate_from = now - timedelta(days=(age_max + 1) * 365)
                birthdate_to = now - timedelta(days=age_min * 365)
                queryset = queryset.filter(
                    birthDate__range=[birthdate_from, birthdate_to]
                )
            except ValueError:
                return Response(
                    {"error": "Invalid age value provided."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return queryset
