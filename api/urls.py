from django.urls import path, include
from . import views
from . views import clientviewset, projectviewset, userviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clients', clientviewset)
router.register(r'projects', projectviewset)
router.register(r'users',userviewset)

urlpatterns = [
    path("", include(router.urls))
]