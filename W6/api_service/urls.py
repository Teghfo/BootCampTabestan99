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
    path('salon', views.SalonList.as_view(), name='salon'),
    path('salon/<int:pk>', views.SalonDetail.as_view(), name='salon-detail'),
    path('movies', views.MovieView.as_view()),
    path('hello', views.hello),
    path('comments', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment-detail'),
    path('articles', views.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name='article-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
