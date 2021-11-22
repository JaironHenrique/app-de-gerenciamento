from django.conf.urls import url
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def servicos(request):
    return render(request, "servicos/servicos_atv.htm")

def criar_atv(request):
    return render(request, "servicos/criar_atv.htm")

def desempenho(request):
    return render(request, "servicos/servicos_desempenho.htm")

def pomodoro(request):
    return render(request, "servicos/servicos_pomodoro.htm")