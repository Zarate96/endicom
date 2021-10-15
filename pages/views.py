from django.shortcuts import render, redirect
from .models import Proyectos
from django.views.generic.detail import DetailView
#from .decorators import check_recaptcha
#from django.contrib import messages

def home(request):
    proyectos = Proyectos.objects.all()
    return render(request, 'pages/home.html', {'proyectos':proyectos})

class ProyectoDetailView(DetailView):
    """Detail post."""
    template_name = 'pages/proyectoDetalle.html'
    model = Proyectos
    context_object_name = 'proyecto'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos'] = Proyectos.objects.all()
        return context



