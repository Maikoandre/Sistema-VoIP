from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ramais.views import ExtensionViewSet

router = DefaultRouter()
router.register(r'extensions', ExtensionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
