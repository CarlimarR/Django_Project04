from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm  # Asegúrate de importar el formulario adecuado

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm  # Asegúrate de importar el formulario adecuado
    success_url = reverse_lazy('post_list')  # Redirige a la página de inicio de sesión después del registro

# Create your views here.

#mostratra la vista de inicio de sesion
def start(request):
    return render(request, 'post_start.html')  # Asegúrate de tener un template llamado home.html