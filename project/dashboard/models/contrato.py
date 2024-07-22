from django.db import models
from .auto import Auto
from .cliente import Cliente
    

class Contrato(models.Model):


    ini_cont = models.DateField(help_text="Inicio de contrato")
    cuota = models.FloatField(help_text="Cuota Semanal")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    auto = models.OneToOneField(Auto,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.cuota}"


        

