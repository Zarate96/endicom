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
    activa = models.BooleanField(verbose_name="Proyecto activo", default=True)
    url_imagen = models.URLField()
    url = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.url = slugify(self.nombre)
        super(Proyectos, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f"/proyectos/{self.url}/"

    class Meta:
        verbose_name_plural = "Proyectos"

class Newsletter(models.Model):
    email = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Newsletter"

    def __str__(self):
        return f"{self.email} se suscribio el día {self.fecha}"

class Mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    #telefono = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField(blank=True)
    is_answered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return f"Mensaje enviado por {self.email} el día {self.fecha}, respondido: {self.is_answered} "

class MensajesProyectos(models.Model):
    nombre = models.CharField(max_length=100)
    nombreProyecto = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    mensaje = models.TextField(blank=True)
    is_answered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Mensajes por proyecto"

    def __str__(self):
        return f"Interes enviado por {self.email} el día {self.fecha}, respondido: {self.is_answered}"
