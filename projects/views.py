from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def lista_projetos(request):
    projetos = Project.objects.all()

    contexto = {
        'lista_de_projetos': projetos
    }

    return render(request, 'projects/project_list.html', contexto)

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})
