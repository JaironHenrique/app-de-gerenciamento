from django.urls import path
from servicos import views as views

urlpatterns = [
    path("", views.servicos, name="servicos"),
    path("criar_atv/", views.criar_atv, name="criar_atv"),
    path("desempenho/", views.desempenho, name="desempenho"),
    path("pomodoro/", views.pomodoro, name="pomodoro")
]