from django.shortcuts import render
from .models import Task
from django.views.generic import ListView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/index.html', { 'tasks': tasks })

def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', { 'task': task })

tasks = [
  Task('Build todo app', '9/27/2021', 'Python Project', False),
  Task('Test', '9/28/2021', 'Test', False),
]