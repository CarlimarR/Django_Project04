from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    """
    Modelo básico para publicaciones de usuarios
    """
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to= 'static/upload_imagen', blank=True)   #aqui se registra la direccion de la imagenes (que en este caso estan es static)
    author = models.CharField(max_length=100)

    
    class Meta:
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title