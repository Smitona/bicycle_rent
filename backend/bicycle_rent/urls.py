from django.urls import include, path
from rest_framework.routers import SimpleRouter

from bicycle_rent.views import 

router = SimpleRouter()

app_name = 'bicycle_rent'

urlpatterns = [
    path('', include(router.urls)),
]

