from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks_index, name='tasks_index'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='tasks_detail'),
]
