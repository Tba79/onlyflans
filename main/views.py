from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.pasteles import pasteles

# Create your views here.
def index (request):
    context = {'pasteles': pasteles}
    return render(request, 'index.html', context)
    

def about (request):
    return render(request, 'about.html')

def welcome (request):
    return render(request, 'welcome.html')

def contact_form (request):
    errores = []
    
    customer_name = request.POST['customer_name']
    customer_email = request.POST['customer_email']
    message = request.POST['message']
    
    if len(customer_name) > 6:
        errores.append('Largo mayor a 6')
        
    if  not '@' in customer_email:
        errores.append('Mail no valido, falta tu arroba @ de BB')

    context = {'errores': errores}
    if len(errores) > 0:
        return render(request,'welcome.html', context)
    else:
        
        return render(request, 'contactcheck.html', context)
    
