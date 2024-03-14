from rest_framework import viewsets

from API.models import Client
from API.serializers import ClientSerializer
from API.pagination import ClientPagination


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientPagination
