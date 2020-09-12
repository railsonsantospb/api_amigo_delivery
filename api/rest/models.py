from django.db import models

# Create your models here.
class Client(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.cpf

class Category(models.Model):
    name = models.CharField(max_length=300)
    image = models.TextField(
            db_column='data',
            blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_cpf = models.CharField(max_length=300)

    def __str__(self, name, image, id_cpf):
        self.name = name
        self.image = image
        self.id_cpf = id_cpf
    