from django.urls import include, path
from rest_framework import routers

# from movie.signals import sync
from movie.views import *

router = routers.DefaultRouter()
router.register(r'movie',MovieViewset)



urlpatterns = [
    path('',include(router.urls)),
    # path('sync',sync)
]
