from django.shortcuts import render, redirect
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'projects/index.html')


def projects(request):
    projects = [
        {
            'id': 1,
            'title': "PROJECT A"
        },
        {
            'id': 2,
            'title': "PROJECT B"
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
    context = {'project': project, 'project_tasks': project_tasks}
    return render(request, 'projects/project-detail.html', context)


def taskList(request):
    user_tasks = Task.objects.filter(assignee=request.user)
    tasks = Task.objects.filter(assignee=None)
    context = {'tasks': tasks, 'user_tasks': user_tasks}
    return render(request, 'tasks/tasks.html', context)


def taskDetail(request, pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task': task}
    return render(request, 'tasks/task-detail.html', context)


def taskCreate(request):
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context = {'form': form}
    return render(request, 'tasks/task-create.html', context)


class ProjectCreateView(CreateView):
    model = Project
    fields= ['name', 'description']
    template_name = 'projects/project-create-form.html'
    success_url = reverse_lazy('projects')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project-update-form.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task-update-form.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task-confirm-delete.html'
    success_url = reverse_lazy('tasks')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project-confirm-delete.html'
    success_url = reverse_lazy('projects')
