from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ramais.views import ExtensionViewSet, MakeCallView

router = DefaultRouter()
router.register(r'extensions', ExtensionViewSet)
router.register(r'make-call', MakeCallView, basename='make-call')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # path('api/', include(router.urls)),
    path('api/make-call/', MakeCallView.as_view(), name='make-call'),
]
