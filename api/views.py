from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoSerializer
from .models import ToDo

class ToDoView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer