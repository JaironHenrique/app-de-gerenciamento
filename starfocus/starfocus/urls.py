"""starfocus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from starfocus import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("servicos/", views.servicos, name="servicos"),
    path("criar_atv/", views.criar_atv, name="criar_atv"),
    path("desempenho/", views.desempenho, name="desempenho"),
    path("pomodoro/", views.pomodoro, name="pomodoro"),
    path("login/", views.login, name="login"),
    path("criar_conta/", views.criar_conta, name="criar_conta"),
    path("desenvolvedores/", views.desenvolvedores, name="desenvolvedores"),
    path('atividades/', include('atividades.urls')),
    path('produtividade_ao_longo_do_tempo/', include('produtividade_tempo.urls')),
    path('top/', include('top.urls')),
    path('semana/', include("semana.urls")),
]
