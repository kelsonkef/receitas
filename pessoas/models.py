from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    # Parecido comum SubString
    def __str__(self):
        return self.nome
