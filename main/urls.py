from django.urls import path #siempre va importa path
from main.views import index, about, welcome, contact_form #importa las funciones

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('contact_form', contact_form),
]