from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name='api'),
    path('accounts/', views.listAccounts, name='list-accounts'),
    path('accounts/<str:pk>/', views.getSpecificAccount, name='list-account'),
    path('create-account/', views.createAccount, name='create-account'),
    path('update-account/<str:pk>/', views.updateAccount, name='update-account'),
    path('delete-account/<str:pk>/', views.deleteAccount, name='delete-account'),
]