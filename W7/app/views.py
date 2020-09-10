from rest_framework import viewsets

from .serializers import PublicationListSerializer, PublicationRetrieveSerializer
from .models import Publication


class PublicationView(viewsets.ModelViewSet):

    serializers = {
        'list': PublicationListSerializer,
        'retrieve': PublicationRetrieveSerializer
    }

    def get_queryset(self):
        return Publication.objects.filter(rant=True)

    def get_serializer_class(self):
        return self.serializers.get(self.action)
