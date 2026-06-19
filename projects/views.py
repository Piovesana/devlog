from django.shortcuts import render
from .models import Project

def lista_projetos(request):
    projetos = Project.objects.all()

    contexto = {
        'lista_de_projetos': projetos
    }

    return render(request, 'projects/project_list.html', contexto)
