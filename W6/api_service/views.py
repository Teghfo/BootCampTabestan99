from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from cinema.models import Movie, Cinema, Salon
from .serializers import MovieSerializer, SalonSerializer, CinemaSerializer


class MovieView(APIView):

    def get(self, request, format=None):
        print(request.content_type)
        movies = Movie.objects.all()
        movie_serialized = MovieSerializer(movies, many=True)
        return Response(movie_serialized.data)


class SalonView(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer


class CinemaView(viewsets.ModelViewSet):
    queryset = Cinema.objects.all().order_by('name')
    serializer_class = Cinema


@api_view()
def hello(request):
    print(request)
    return HttpResponse('Hello')
