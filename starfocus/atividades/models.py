from datetime import datetime
from django.db import models

class Atividade(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)
    duracao = models.IntegerField()
    data = models.DateField()
    
    def __str__(self) -> str:
        return f"Nome: {self.nome} - Descrição: {self.descricao} - Duração: {self.duracao} - Data: {self.data}"
    
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    tempo = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Nome: {self.nome} - Tempo: {self.tempo}"