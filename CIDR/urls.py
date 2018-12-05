# from django.urls import path

from rest_framework import routers
from store.views import NetworkViewset


router = routers.SimpleRouter()
router.register(r'store', NetworkViewset)

urlpatterns = router.urls
