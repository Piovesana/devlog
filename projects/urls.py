from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('novo/', views.criar_projeto, name='criar_projeto'),
]

