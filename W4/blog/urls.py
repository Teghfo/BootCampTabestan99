from django.urls import path, include

from .views import index_blog, HomePageView

urlpatterns = [
    path('index/', HomePageView.as_view(), name='index-blog'),
]
