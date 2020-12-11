from rest_framework import routers
from django.urls import path
from .views import AccountViewSet, CreateAccountView, DeleteAccountView

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('create-account', CreateAccountView.as_view()),
    path('delete-account/<int:pk>', DeleteAccountView.as_view())
]

urlpatterns += router.urls