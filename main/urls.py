from django.urls import path #siempre va importa path
from . import views #importa las funciones



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('contactcheck/', views.contactcheck, name='contactcheck'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]