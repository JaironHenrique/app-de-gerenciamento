from django.urls import path
from semana import views

urlpatterns = [
    path("", views.dias, name="dias")
]