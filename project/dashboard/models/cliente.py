from django.db import models
    
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=20, help_text="Nombre")
    apellidos =models.CharField(max_length=100, help_text="Apellidos")
    num_doc = models.CharField(max_length=50, help_text="Número de documento")

    def __str__(self):
        return f"{self.num_doc}"

