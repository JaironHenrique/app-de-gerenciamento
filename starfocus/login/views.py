from django.conf.urls import url
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def login(request):
    return render(request, "login/login.htm")

def criar_conta(request):
    return render(request, "login/criar_conta.htm")