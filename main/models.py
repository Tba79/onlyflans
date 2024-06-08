from django.db import models

# Create your models here.

class Contact(models.Model):
    nombre = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)
    mensaje = models.CharField(max_length = 100)