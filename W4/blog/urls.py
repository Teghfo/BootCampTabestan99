from django.urls import path, include

from .views import index_blog, HomePageView, ArticleDetail

urlpatterns = [
    path('index/', HomePageView.as_view(), name='index-blog'),
    path('<str:slug>/', ArticleDetail.as_view(), name='detail-article'),
]
