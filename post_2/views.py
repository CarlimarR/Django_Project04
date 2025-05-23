from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Publicacion
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView




# Create your views here.

class PostListView(ListView):
    template_name = "post_list.html"
    model = Publicacion
    context_object_name = 'posts'                           # con este comando se puede modificar el nombre de las listas que se muestran en el template

class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Publicacion
    fields = ['title', 'description', 'image', 'author']
    success_url = reverse_lazy('post_list')                  #redirecciona a la vista post_list cuando se crea una publicacion

class PostDetailsView(DetailView):
    template_name = "post_details.html"
    model = Publicacion

    #fields = '__all__'  esto coloca todos los datos que tiene el 
    
    
#MODIFICAR

class PostUpdateView(UpdateView):
    model = Publicacion
    template_name = 'post_update.html'  # Template para el formulario de edición
    fields = ['title', 'description', 'image', 'author']  # Campos editables
    success_url = '/'  # URL a la que redirigir tras guardar


#MODIeliminar

class PostDeleteView(DeleteView):
    model = Publicacion
    template_name = 'post_delete.html'  # Template de confirmación
    success_url = '/'  # URL a la que redirigir tras eliminar