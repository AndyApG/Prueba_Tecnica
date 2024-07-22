from django.db import models

class Auto(models.Model):


    marca = models.CharField(max_length=20, help_text="Marca")
    modelo = models.CharField(max_length=20, help_text="Modelo")
    placa = models.CharField(max_length=10, help_text="Placa")
   
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.placa}"
    