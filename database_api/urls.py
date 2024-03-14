from django.contrib import admin
from django.urls import path, include

from API import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("API.urls", namespace="clients")),
]
