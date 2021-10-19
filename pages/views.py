from django.shortcuts import render, redirect
from .models import Proyectos, Mensajes, Newsletter, MensajesProyectos
from django.views.generic.detail import DetailView
from .decorators import check_recaptcha
from django.contrib import messages

def home(request):
    proyectos = Proyectos.objects.all().filter(activa=True)
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
        slug = self.kwargs['url']
        context['proyectos'] = Proyectos.objects.all().filter(activa=True).exclude(url=slug)
        return context

@check_recaptcha
def mensaje(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

    if request.recaptcha_is_valid:    
        mensaje = Mensajes(nombre=name, email=email, asunto=subject, mensaje=message)
        mensaje.save()
        messages.success(request, 'Tu mensaje ha sido enviado, nos pondremos en contacto contigo en breve.')
        #return redirect('home')

    else:
        messages.error(request, 'Porfavor verifique la información')
        #return redirect('home')

    return redirect('home')
    #return render(request, 'pages/home.html', {})

@check_recaptcha
def mensajeProyecto(request):
    if request.method == 'POST':
        proyecto = request.POST['namePro']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']

    if request.recaptcha_is_valid:    
        mensaje = MensajesProyectos(nombre=name, nombreProyecto=proyecto, email=email, telefono=phone, mensaje=comment)
        mensaje.save()
        messages.success(request, 'Tu interes ha sido registrado, nos pondremos en contacto contigo en breve.')
        #return redirect('home')

    else:
        messages.error(request, 'Porfavor verifique la información')
        #return redirect('home')

    return redirect('home')
    #return render(request, 'pages/home.html', {})

@check_recaptcha
def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']

    if request.recaptcha_is_valid:
        if email == "":
            messages.error(request, 'Porfavor verifique la información')
        else:
            mensaje = Newsletter(email=email)
            mensaje.save()
            messages.success(request, 'Gracias por suscribirte.')
        #return redirect('home')
    
    else:
        messages.error(request, 'Porfavor verifique la información')
        #return redirect('home')

    return redirect('home')
    #return render(request, 'pages/home.html', {})


