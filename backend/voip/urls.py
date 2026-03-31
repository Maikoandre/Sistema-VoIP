from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ramais.views import ExtensionViewSet, MakeCallView, index # <--- NOVO: Importe o 'index' aqui

router = DefaultRouter()
router.register(r'extensions', ExtensionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    
    # --- ROTA PARA O SEU FRONTEND ---
    path('', index, name='index'), # <--- NOVO: Isso faz o seu HTML ser a página inicial
    
    # --- ROTAS DA API ---
    path('api/', include(router.urls)), # Reativei para os ramais aparecerem na API
    path('api/make-call/', MakeCallView.as_view(), name='make-call'),
]