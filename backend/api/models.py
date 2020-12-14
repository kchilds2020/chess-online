from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    total_games = models.IntegerField(default = 0)
    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add=True)
    active_games = models.JSONField(default = dict)
    
    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Queue(models.Model):
    username = models.CharField(max_length=100)

class Match(models.Model):
    white = models.CharField(max_length=100)
    black = models.CharField(max_length=100)
    turn = models.CharField(max_length=100, default='white')
    winner = models.CharField(max_length=100, default = 'pending')
    board = models.TextField(default = '')
    date_created = models.DateTimeField(auto_now_add=True)
    match_record = models.TextField(default = '')
    