from django.urls import path
from produtividade_tempo import views

urlpatterns = [
    path("", views.pagina, name="pagina")
]