from django.db import models

# Create your models here.
class ToDo(models.Model):
    todo_item = models.CharField(max_length=100, default='')
    completed = models.BooleanField(default=False)