from django.urls import path
from atividades import views

urlpatterns = [
    path("registrar/", views.registrar, name="registrar"),
    path("index/", views.index, name="index")
]