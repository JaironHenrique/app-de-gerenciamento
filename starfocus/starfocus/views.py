from django.conf.urls import url
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, "index.htm")

def desenvolvedores(request):
    return render(request, "desenvolvedores/desenvolvedores.htm")

def login(request):
    return render(request, "login/login.htm")

def criar_conta(request):
    return render(request, "login/criar_conta.htm")

def servicos(request):
    return render(request, "servicos/servicos_atv.htm")

def criar_atv(request):
    return render(request, "servicos/criar_atv.htm")

def pomodoro(request):
    return render(request, "servicos/servicos_pomodoro.htm")