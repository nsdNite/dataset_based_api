from rest_framework.routers import DefaultRouter

from API.views import ClientViewSet

router = DefaultRouter()

router.register(r"clients", ClientViewSet)

urlpatterns = router.urls

app_name = "API"
