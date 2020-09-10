from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)


router.register('publication/', views.PublicationView, basename='publication')


urlpatterns = [
    path('', include(router.urls))
]
