from django.urls import path
from .views import *
urlpatterns = [
    path('',listarTarea, name='listar'),
    path('crear',crearTarea, name='crear')
]