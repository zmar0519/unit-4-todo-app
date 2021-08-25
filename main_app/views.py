from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello world</h1>')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  return render(request, 'tasks/index.html', { 'tasks': tasks })

class Task:
  def __init__(self, name, dueDate, description, isComplete):
      self.name = name
      self.dueDate = dueDate
      self.description = description
      self.isComplete = isComplete

tasks = [
  Task('Build todo app', '9/27/2021', 'Python Project', False),
  Task('Test', '9/28/2021', 'Test', False),
]