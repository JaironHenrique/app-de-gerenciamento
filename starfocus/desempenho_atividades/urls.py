from django.urls import path
from desempenho_atividades import views

urlpatterns = [
    path("", views.visualizacao, name="visualizacao")
]