# tareas/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.editar, name="editar"),
    path("crear/", views.crear, name="crear"),
    path("borrar/<int:id>/", views.borrar, name="borrar")
]