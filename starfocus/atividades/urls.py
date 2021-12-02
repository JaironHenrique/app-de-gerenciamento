from django.urls import path
from atividades import views

urlpatterns = [
    path("registrar/", views.registrar, name="registrar"),
    path("index/", views.index, name="index"),
    path("registrar_user/", views.registrar_user, name="registrar_user"),
    path("index_2/", views.index_2, name="index_2")
]