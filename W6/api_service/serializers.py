from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
