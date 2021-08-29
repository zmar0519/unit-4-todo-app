from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  name = models.CharField(max_length=100)
  dueDate = models.DateField()
  description = models.CharField(max_length=500)
  isComplete = models.BooleanField(default=False)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("tasks_detail", kwargs={"task_id": self.id})
  