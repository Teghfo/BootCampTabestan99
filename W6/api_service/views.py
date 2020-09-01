from rest_framework import viewsets

from cinema.models import Movie
from .serializers import MovieSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
