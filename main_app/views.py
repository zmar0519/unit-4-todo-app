from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

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