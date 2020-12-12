from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=200)
    total_games = models.IntegerField(default = 0)
    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add=True)
    