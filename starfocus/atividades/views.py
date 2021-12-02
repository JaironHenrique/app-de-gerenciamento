from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from atividades.models import Atividade
import random
from datetime import datetime, timedelta
import numpy as np

# Create your views here.

def index(request):
    msg = ""
    lista_atv = Atividade.objects.all()
    for atv in lista_atv:
        msg += str(atv)+"<br>"
    return HttpResponse(msg)

def registrar(request):
    atividades = {"Estudar Cálculo":"Descrição_1", "Estudar Linguagens de Programação":"Descrição_2",
                  "Praticar exercícios físicos":"Descrição_3","Estudar Economia":"Descrição_4",
                  "Fazer atividades":"Descrição_5"}
    lista_atividades = list(atividades.keys())
    datas = np.arange(np.datetime64('2021-01-01'), np.datetime64('2021-12-31'))
    datas = datas.tolist()
    
    for i in range(200):
        duracao = random.randint(1,10)
        nome = random.choice(lista_atividades)
        descricao = atividades[nome]
        data = random.choice(datas)
        atividade = Atividade(nome=nome, descricao=descricao, duracao=duracao, data=data)
        atividade.save()
    
    return HttpResponse("Nome: " + nome + " - Descrição: " + str(descricao) + " - Duração: " + str(duracao) + " - Data: " + str(data))