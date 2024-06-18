# main/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=10,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Ejemplo: Juana FlanLover'
        })
    )
    email = forms.EmailField(
        max_length=20,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Ejemplo: flanlover@flan.com'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'rows': 5,
            'placeholder': 'Ingrese su mensaje'
        })
    )

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repass = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

"""class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repass = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))"""
