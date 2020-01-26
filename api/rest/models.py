from django.db import models

# Create your models here.
class Client(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cpf
    