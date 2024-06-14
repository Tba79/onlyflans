from django.shortcuts import render, redirect
from django.http import HttpResponse
#from main.pasteles import pasteles
from main.forms import ContactForm
from main.models import Contact, Flan
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message="Bienvenido BB"

# Create your views here.
def index (request):
    #debe mostrar todos los flanes de besa de datos
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {'flanes': flanes_publicos}
    return render(request, 'index.html', context)
    

def about (request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm() # Se crea una instancia del formulario contactForm sin datos iniciales.
        context = {'form': form} # Se crea un contexto que contiene el formulario vacío.
        return render(request, 'contact.html', context) # Se renderiza la plantilla 'welcome.html' con el contexto.
    else:
        form = ContactForm(request.POST) # Se crea una instancia de ContactForm con los datos enviados en la solicitud POST.
        if form.is_valid(): # Se verifica si los datos del formulario son válidos.
            form.cleaned_data['source']='desde_welcome'
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('/contactcheck') # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form} # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(request, 'contact.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.


def contactcheck (request):
    return render(request, 'contactcheck.html')




def ayuda (request):
    if request.method == 'GET':
        form = ContactForm() # Se crea una instancia del formulario contactForm sin datos iniciales.
        context = {'form': form} # Se crea un contexto que contiene el formulario vacío.
        return render(request, 'ayuda.html', context) # Se renderiza la plantilla 'welcome.html' con el contexto.
    else:
        form = ContactForm(request.POST) # Se crea una instancia de ContactForm con los datos enviados en la solicitud POST.
        if form.is_valid(): # Se verifica si los datos del formulario son válidos.
            form.cleaned_data['source']='desde_ayuda'
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('/contactcheck') # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form} # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(request, 'ayuda.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.
    
    
@login_required    
def welcome(request):
    #debe mostrar solo los flanes privados de la base de daros
    flanes_privados = Flan.objects.filter(is_private = True)
    context = {'flanes': flanes_privados}
    return render(request, 'welcome.html', context)
    """return render(
        request, 'welcome.html', {'flanes_privados': flanes_privados}
    )"""

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout_view(request):
    logout (request)
    messages.warning(request, "Nos vemos pronto BB")
    return redirect ('/')