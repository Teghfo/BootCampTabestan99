from django.urls import path
from .views import film_detail, all_films

urlpatterns = [
    path('details/<int:film_id>', film_detail, name='film-detail'),
    path('films/', all_films, name='films-list'),

]
