from django.urls import path #siempre va importa path
from main.views import index #importa las funciones

urlpatterns = [
    path('', index)
]