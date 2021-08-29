from django.shortcuts import redirect, render
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('task_index')
    else:
      error_message = "Invalid Sign up = try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)  

tasks = [
  Task('Build todo app', '9/27/2021', 'Python Project', False),
  Task('Test', '9/28/2021', 'Test', False),
]

class TaskCreate(CreateView):
  model = Task
  fields = 'name', 'dueDate', 'description'
  success_url = '/tasks/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(UpdateView):
  model = Task
  fields = '__all__'

class TaskDelete(DeleteView):
  model = Task
  success_url = '/tasks/'

class Home(LoginView):
  template_name = 'home.html'