from django.urls import path
from desenvolvedores import views as views

urlpatterns = [
    path("", views.desenvolvedores, name="desenvolvedores"),
]