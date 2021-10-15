from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(
    route='<slug:url>/',
    view=views.ProyectoDetailView.as_view(),
    name='detail'
),
]
    