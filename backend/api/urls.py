from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name='api'),
    path('check-session/', views.checkSession, name='check-session'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('accounts/', views.listAccounts, name='list-accounts'),
    path('accounts/<str:pk>/', views.getSpecificAccount, name='list-account'),
    path('create-account/', views.createAccount, name='create-account'),
    path('update-account/<str:pk>/', views.updateAccount, name='update-account'),
    path('delete-account/<str:pk>/', views.deleteAccount, name='delete-account'),
]