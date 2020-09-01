from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('movie', views.MovieView)


urlpatterns = [
    path('', include(router.urls))
]
