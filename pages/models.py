from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify

ETAPAS = (
    ('Planeación','Planeación'),
    ('Desarrollo','Desarrollo'),
    ('Despliegue','Despliegue'),
    ('Producción','Producción'),
)

class Proyectos(models.Model):
    nombre = models.CharField(verbose_name="Nombre del proyecto", max_length=100)
    descripcion_corta = models.CharField(verbose_name="Descripción corta", max_length=100)
    etapa = models.CharField(verbose_name="Etapa", choices=ETAPAS, max_length=100)
    contenido = RichTextField(verbose_name="Información completa")
    fecha = models.DateTimeField(default=timezone.now)
    url_imagen = models.URLField()
    url = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.url = slugify(self.nombre)
        super(Proyectos, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Proyectos"