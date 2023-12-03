from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'projects/index.html')

def projects(request):
     projects = [
       {
        'id':1,
        'title':"PROJECT A"
       },
       {
        'id':2,
        'title':"PROJECT B"
       }]
     context = {'projects': projects}
     return render(request, 'projects/projects.html', context)


def projectList(request):
     project = Project.objects.all()
     context = {'projects': project}
     return render(request, 'projects/projects.html', context)


def projectDetail(request, pk):
     project = get_object_or_404(Project, id=pk)
     project_tasks = project.task_set.all()
     context = {'project':project, 'project_tasks':project_tasks}
     return render(request, 'projects/project-detail.html', context)
