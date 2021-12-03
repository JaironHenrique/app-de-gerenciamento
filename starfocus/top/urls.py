from django.urls import path
from top import views

urlpatterns = [
    path("<int:quant>", views.pagina, name="pagina")
]