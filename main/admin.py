from django.contrib import admin
from main.models import Contact, Flan

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, PersonaAdmin)


class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flan, FlanAdmin)