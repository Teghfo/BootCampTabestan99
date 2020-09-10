from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PublicationListSerializer, PublicationRetrieveSerializer, ArticleListSerializer, ArticleRetrieveSerializer
from .models import Publication, Article


class PublicationView(viewsets.ReadOnlyModelViewSet):

    lookup_field = 'slug'

    serializers = {
        'list': PublicationListSerializer,
        'retrieve': PublicationRetrieveSerializer
    }

    def get_queryset(self):
        return Publication.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    @action(methods=['get'], detail=True, url_path='set-rant-true', url_name='set_true')
    def set_rant(self, request, slug=None):
        obj = self.get_object()
        obj.rant = True
        obj.save()
        return Response(status=200)


class ArticleView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    lookup_field = 'slug'

    serializers = {
        'list': ArticleListSerializer,
        'retrieve': ArticleRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)


class PublicationBasicView(APIView):

    def get(self, request):
        queryset = Publication.objects.all()
        serializer = PublicationListSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
