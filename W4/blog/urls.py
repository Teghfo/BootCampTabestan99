from django.urls import path, include

from .views import index_blog, ArticleDetail, SearchArticle, ArticleList, CreateArticleView

urlpatterns = [
    path('index/', index_blog.as_view(), name='index-blog'),
    path('<str:slug>/', ArticleDetail.as_view(), name='detail-article'),
    path('search', SearchArticle.as_view(), name='search-articles'),
    path('list', ArticleList.as_view(), name='list-articles'),
    path('abc', CreateArticleView.as_view(), name='create-article'),
]
