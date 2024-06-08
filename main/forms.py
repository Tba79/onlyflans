from django import forms

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
        label='Correo Electronico',
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


