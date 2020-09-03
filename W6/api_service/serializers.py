from rest_framework import serializers

from cinema.models import Movie, Salon, Cinema


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    salon = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Salon.objects.all())

    class Meta:
        model = Cinema
        fields = ['name', 'salon']


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'
