from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
# router.register('movie', views.MovieView)
# router.register('salon', views.SalonView)
# router.register('cinema', views.CinemaView)


urlpatterns = [
    # path('', include(router.urls)),
    path('movies', views.MovieView.as_view()),
    path('hello', views.hello)
]

urlpatterns = format_suffix_patterns(urlpatterns)
