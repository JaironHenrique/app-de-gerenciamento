from django.urls import path
from top import views

urlpatterns = [
    path("<int:quant>", views.top_user, name="top_user")
]