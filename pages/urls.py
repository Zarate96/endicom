from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/<slug:url>/', view=views.ProyectoDetailView.as_view(), name='detail'),
    path('mensaje/', views.mensaje, name='mensaje'),
    path('mensajeproyecto/', views.mensajeProyecto, name='mensaje-proyecto'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
    