from rest_framework import serializers

from .models import Publication, Article


class PublicationListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publication
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        fields = ['url', 'id', 'name']


class PublicationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'
