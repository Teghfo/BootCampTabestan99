from rest_framework import serializers

from cinema.models import Movie, Salon, Cinema


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class SalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'
