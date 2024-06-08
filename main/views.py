from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.pasteles import pasteles
from main.forms import ContactForm
from main.models import Contact

# Create your views here.
def index (request):
    context = {'pasteles': pasteles}
    return render(request, 'index.html', context)
    

def about (request):
    return render(request, 'about.html')


def welcome(request):
    if request.method == 'GET':
        form = ContactForm() # Se crea una instancia del formulario contactForm sin datos iniciales.
        context = {'form': form} # Se crea un contexto que contiene el formulario vacío.
        return render(request, 'welcome.html', context) # Se renderiza la plantilla 'welcome.html' con el contexto.
    else:
        form = ContactForm(request.POST) # Se crea una instancia de ContactForm con los datos enviados en la solicitud POST.
        if form.is_valid(): # Se verifica si los datos del formulario son válidos.
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('/contactcheck') # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form} # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(request, 'welcome.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.


def contactcheck (request):
    return render(request, 'contactcheck.html')




def ayuda (request):
    form = ContactForm() #Se crea instancia del formulario
    context ={'form':form} #Se crea contexto que contienen formulario
    return render(request, 'ayuda.html', context) #Renderiza plantilla 
    
