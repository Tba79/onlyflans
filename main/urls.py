from django.urls import path #siempre va importa path
from main.views import index, about, welcome #importa las funciones

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    
]