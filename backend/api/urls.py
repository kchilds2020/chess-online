from rest_framework import routers
from .api import AccountViewSet

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet, 'accounts')

urlpatterns = router.urls