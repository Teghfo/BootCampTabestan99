from rest_framework import serializers

from .models import Publication, Article


class PublicationListSerializer(serializers.HyperlinkModelSerializer):

    class Meta:
        model = Publication
        fields = ['url', 'id', 'name']


class PublicationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ['id', 'title', 'publication', 'author', 'detail']
