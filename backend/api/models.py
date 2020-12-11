from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    total_games = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)