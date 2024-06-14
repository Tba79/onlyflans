from django.urls import path #siempre va importa path
from main.views import index, about, welcome, ayuda, contactcheck, contact, login, register, logout_view #importa las funciones



urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('contact/', contact),
    path('ayuda/', ayuda),
    path('contactcheck/', contactcheck),
    #path('login/', login),
    path('register/', register),
    path('logout/', logout_view, name='logout'),

    
    
]