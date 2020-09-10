from rest_framework import serializers

from .models import Publication, Article


class PublicationListSerializer(serializers.HyperlinkedModelSerializer):

    # name_pub = serializers.CharField(source='name')
    article = serializers.HyperlinkedRelatedField(
        view_name='article-detail', lookup_field='slug', many=True, read_only=True)

    class Meta:
        model = Publication
        extra_kwargs = {'url': {'lookup_field': 'slug'},
                        'name': {'write_only': True}}
        fields = ['url', 'id', 'name', 'article']


class PublicationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'


class ArticleListSerializer(serializers.HyperlinkedModelSerializer):

    # name_pub = serializers.CharField(source='name')

    class Meta:
        model = Article
        extra_kwargs = {'url': {'lookup_field': 'slug'},
                        'publication': {'lookup_field': 'slug'}}
        exclude = ['slug', 'author']


class ArticleRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
