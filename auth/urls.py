from django.urls import path, include
from .views import SignupView, start  # Asegúrate de importar la vista de registro


urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),  # URL para las vistas de autenticación de Django (login, logout, etc.)
    path('signup/', SignupView.as_view(), name='signup'),  # URL para la vista de 
    path('', start, name='start'),  # URL para la vista de inicio
]