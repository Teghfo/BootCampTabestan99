from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    name = models.CharField(max_length=50)
    rant = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    publication = models.ForeignKey(
        Publication, related_name='article', on_delete=models.CASCADE)
    author = models.ManyToManyField(User)
    detail = models.TextField()
    published = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title
