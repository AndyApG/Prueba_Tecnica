from django.contrib import admin
from .models.auto import Auto
from .models.cliente import Cliente
from .models.contrato import Contrato

admin.site.register(Auto)
admin.site.register(Cliente)
admin.site.register(Contrato)

