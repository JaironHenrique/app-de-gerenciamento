from django.urls import path
from login import views as views

urlpatterns = [
    path("", views.login, name="login"),
    path("criar_conta/", views.criar_conta, name="criar_conta"),
]