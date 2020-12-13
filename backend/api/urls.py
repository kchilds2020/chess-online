from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name='api'),
    path('login/', views.login, name='login'),
    path('users/', views.listUsers, name='list-users'),
    path('users/<str:pk>/', views.getSpecificUser, name='list-user'),
    path('create-user/', views.createUser, name='create-user'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('delete-user/<str:pk>/', views.deleteUser, name='delete-user'),
]