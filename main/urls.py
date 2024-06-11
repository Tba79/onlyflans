from django.urls import path #siempre va importa path
from main.views import index, about, welcome, ayuda, contactcheck, contact  #importa las funciones

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('contact/', contact),
    path('ayuda/', ayuda),
    path('contactcheck/', contactcheck),
    
]