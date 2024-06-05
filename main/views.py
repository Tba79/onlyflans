from django.shortcuts import render
from main.pasteles import pasteles

# Create your views here.
def index (request):
    context = {'pasteles': pasteles}
    return render(request, 'index.html', context)
    

def about (request):
    return render(request, 'about.html')

def welcome (request):
    return render(request, 'welcome.html')


