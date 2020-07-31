from django.db import models

class BaseCinemaModel(models.Model):
    genre_choices = [
        ('A', 'Action'), 
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('S', 'Science Fiction')
    ]

    genre = models.CharField(max_length=1, choices=genre_choices)
    


class Films(BaseCinemaModel):
    pass