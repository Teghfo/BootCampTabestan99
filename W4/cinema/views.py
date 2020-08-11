from django.shortcuts import render, get_object_or_404

from .models import Movie


def film_detail(request, film_id):
    if request.method == 'GET':
        obj = get_object_or_404(Movie, pk=film_id)
        context = {
            'movie': obj
        }
    return render(request, 'film-detail.html', context)


def all_films(request):

    if request.method == 'GET':
        q = Movie.objects.all()

    return render(request, 'films-list.html', {'movies': q})
