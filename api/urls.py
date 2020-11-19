from django.contrib import admin
from django.urls import path
from .views import ToDoView

urlpatterns = [
    path('', ToDoView.as_view()),
]
