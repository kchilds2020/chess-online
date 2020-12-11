from rest_framework import routers
from .api import AccountViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = router.urls