from django.contrib import admin
from .models import Proyectos, Mensajes, Newsletter, MensajesProyectos

class MensajestAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'asunto', 'is_answered')
    search_fields = ('nombre', 'email')
    list_per_page = 10

admin.site.register(Mensajes, MensajestAdmin)

admin.site.register(Proyectos)

admin.site.register(Newsletter)

class MensajesProyectotAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'asunto', 'is_answered')
    search_fields = ('nombre', 'email')
    list_per_page = 10

admin.site.register(MensajesProyectos, MensajesProyectotAdmin)