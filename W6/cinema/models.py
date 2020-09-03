from django.db import models


class BaseCinemaModel(models.Model):
    genre_choices = [
        ('A', 'Action'),
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('S', 'Science Fiction')
    ]

    genre = models.CharField(max_length=1, choices=genre_choices)

    class Meta:
        abstract = True


LANGUAGE_CHOICES = [
    ('english', 'English'),
    ('french', 'French'),
    ('spanish', 'Spanish'),
    ('persian', 'Persian'),

]


class Movie(BaseCinemaModel):
    name = models.CharField('نام فیلم', max_length=50)
    cast = models.TextField('بازیگران')
    director = models.CharField('کارگردان', max_length=50)
    language = models.CharField(
        'زبان', max_length=10, choices=LANGUAGE_CHOICES)
    duration_time = models.SmallIntegerField('زمان', help_text='زمان به دقیقه')
    rate = models.FloatField()
    poster = models.ImageField(upload_to='films')
    year = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=50)
    salon_number = models.SmallIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Salon(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
