from django.contrib import admin
from .models import Moeda, Transacao

# Register your models here.

admin.site.register(Moeda)
admin.site.register(Transacao)
