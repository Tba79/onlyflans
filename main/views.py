from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from .forms import ContactForm, RegisterForm
from .models import Contact, Flan
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message = "¡Bienvenido BB!"

def index(request):
    flanes_publicos = Flan.objects.filter(tipo_flan='publico')
    context = {'flanes': flanes_publicos}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def product(request):
    if request.user.is_authenticated:
        # Si el usuario está autenticado, muestra todos los flanes
        flanes = Flan.objects.all()
    else:
        # Si el usuario no está autenticado, muestra flanes públicos y mayores de 18
        flanes = Flan.objects.filter(tipo_flan__in=['publico', 'mayores'])

    return render(request, 'product.html', {'flanes': flanes})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact.html', context)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['source'] = 'desde_welcome'
            Contact.objects.create(**form.cleaned_data)
            return redirect('/contactcheck')
        context = {'form': form}
        return render(request, 'contact.html', context)

def contactcheck(request):
    return render(request, 'contactcheck.html')

def ayuda(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(request, 'ayuda.html', context)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['source'] = 'desde_ayuda'
            Contact.objects.create(**form.cleaned_data)
            return redirect('/contactcheck')
        context = {'form': form}
        return render(request, 'ayuda.html', context)

@login_required
def premium(request):
    flanes_premium = Flan.objects.filter(tipo_flan='premium')
    context = {'flanes': flanes_premium}
    return render(request, 'product.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('home')
        else:
            username = request.POST.get('username')
            if not username:
                messages.error(request, 'Debes ingresar un nombre de usuario.')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos. Verifica tus datos e intenta nuevamente.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
            return redirect('home')
    else:
        form = RegisterForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    messages.warning(request, "¡Nos vemos pronto BB!")
    return redirect('/')

def verificar_edad(request, flan_id):
    try:
        flan = Flan.objects.get(pk=flan_id)
    except Flan.DoesNotExist:
        messages.error(request, "El flan no existe.")
        return redirect('index')
    
    if request.method == 'POST':
        es_mayor_de_18 = True  # Simulación, ajusta según tu lógica real
        
        if es_mayor_de_18:
            messages.success(request, f"¡Has verificado que eres mayor de 18 años para comprar {flan.nombre}!")
            return redirect('product')
        else:
            messages.error(request, "Debes ser mayor de 18 años para comprar este flan.")
            return render(request, 'age_gate.html', {'flan': flan})
    
    return render(request, 'age_gate.html', {'flan': flan})
