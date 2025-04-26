from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm  # Asegúrate de importar el formulario adecuado

class SignupView(CreateView):
    template_name = "authentication/signup.html"
    form_class = UserCreationForm  # Asegúrate de importar el formulario adecuado
    success_url = reverse_lazy('login')  # Redirige a la página de inicio de sesión después del registro

# Create your views here.
