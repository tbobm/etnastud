from django.urls import path, include
from rest_framework import routers

from tane.views import StudentViewset


router = routers.DefaultRouter()
router.register(r'students', StudentViewset)


urlpatterns = [
    path('api/', include(router.urls))
]
