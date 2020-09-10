from django.urls import path, include
from rest_framework import routers

from . import views


class CustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-kasra',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        routers.DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]


router = routers.DefaultRouter(trailing_slash=False)


router.register('publication', views.PublicationView, basename='publication')
router.register('article', views.ArticleView)

urlpatterns = [
    path('', include(router.urls)),
    # path('publication', views.PublicationView.as_view(
    #     {'get': 'list'}), name='publication-list'),
    # path('publication/<slug:slug>', views.PublicationView.as_view(
    #     {'get': 'retrieve'}), name='publication-detail')
    path('basepub', views.PublicationBasicView.as_view()),
]
