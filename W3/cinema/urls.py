from django.urls import path
from .views import film_detail

urlpatterns = [
    path('details/<int:film_id>', film_detail, name='film-detail'),

]