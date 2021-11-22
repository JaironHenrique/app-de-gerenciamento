from django.conf.urls import url
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, "index.htm")