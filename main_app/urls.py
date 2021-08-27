from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks_index, name='tasks_index'),
    path('tasks/<int:task_id>/', views.tasks_detail, 
    name='tasks_detail'),
    path('tasks/create/', views.TaskCreate.as_view(), 
    name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), 
    name='tasks_update'),
    path('tasks_<int:pk>/delete/', views.TaskDelete.as_view(),
    name='tasks_delete'),
]
