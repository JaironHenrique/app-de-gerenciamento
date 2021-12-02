from django.contrib import admin

# Register your models here.
from .models import Atividade,Usuario

admin.site.register(Atividade)
admin.site.register(Usuario)