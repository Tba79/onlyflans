from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=10,
        label='Nombre:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Ingrese nombre aquí'
        })
    )
    email = forms.EmailField(
        max_length=20,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Ingrese correo aquí'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje:',
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'rows': 5,
            'placeholder': 'Ingrese mensaje'
        })
    )




























#from django import forms






# # class ContactForm(forms.Form):
#     nombre = forms.CharField(
#         max_length=15,
#         label = 'nombre: ',
#         widget = forms.TextInput(attrs={
#             'class':'form-control mb-3',
#             'placeholder': 'Nombre de BB',
#         })
#     )
#     email = forms.EmailField(
#         max_length=15,
#         label = 'Mail',
#         widget = forms.EmailInput(attrs={
#             'class':'form-control  ',
#             'placeholder': 'Mail de BB',
#         })
#     )
#     mensaje= forms.CharField(
#     max_length=60,
#     label = 'Mensaje',
#     widget = forms.Textarea(attrs={
#         'class':'form-control mb-3',
#         'placeholder': 'Menajse de BB',
#         'row' : 5
#         })
#     )