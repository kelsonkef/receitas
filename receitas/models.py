from django.db import models
from datetime import datetime #importa o modulo de tempo do Django
from pessoas.models import Pessoa
from django.contrib.auth.models import User
# Create your models here.

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete= models.CASCADE)# informa que estou fazendo um relacionamento com a tabela de Pessoa, o on_delete significa que se eu deletar uma pessoa automaticamente será deletas as suas receitas.
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank = True)

    