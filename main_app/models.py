from django.db import models

# Create your models here.
class Task(models.Model):
  name = models.CharField(max_length=100)
  dueDate = models.DateField()
  description = models.CharField(max_length=500)
  isComplete = models.BooleanField(default=False)

  def __str__(self):
    return self.name