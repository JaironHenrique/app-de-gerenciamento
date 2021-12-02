from django.urls import path
from atividades import views

urlpatterns = [
    # path("registrar/", views.registrar, name="registrar"),
    # path("registrar_user/", views.registrar_user, name="registrar_user"),
    path("mostrar_atvs/", views.mostrar_atvs, name="mostrar_atvs"),
    path("mostrar_users/", views.mostrar_users, name="mostrar_users")
]