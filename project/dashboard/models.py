from django.db import models

from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=20, help_text="Marca")
    modelo = models.CharField(max_length=20, help_text="Modelo")
    placa = models.CharField(max_length=10, help_text="Placa")
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.marca+ " " + self.modelo + " " +self.placa
    
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=20, help_text="Nombre")
    apellidos =models.CharField(max_length=100, help_text="Apellidos")

    ...
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre +' '+ self.apellidos


class Contrato(models.Model):
    num_doc = models.CharField(max_length=50, help_text="Número de documento")
    ini_cont = models.DateField(help_text="Inicio de contrato")
    cuota = models.FloatField(help_text="Cuota Semanal")
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    auto = models.OneToOneField(Auto,on_delete=models.CASCADE)


    class Meta:
        ordering = ["ini_cont"]

    def __str__(self):
        return str(self.cuota)


        

