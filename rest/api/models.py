from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    idade = models.IntegerField()
    
    def __str__(self):
        return self.cpf
    
    
