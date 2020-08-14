from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from user_profile.models import Profile


class Author(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    rate = models.FloatField()

    def __str__(self):
        return self.full_name

    def update_rate(self, new_rate):

        self.rate = new_rate


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    poster = models.ImageField(upload_to='blog/images/')
    author = models.ManyToManyField(Author)
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField()
    rate_article = models.FloatField()
    video = models.FileField(upload_to='blog/videos/', null=True, blank=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title


class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/images/')


RATE_CHOICE = {
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
}


class BaseComment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE_CHOICE, null=True, blank=True)
    is_show = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Comment(BaseComment):
    pass
    # def save(self, *args, **kwargs):
    #     self.article.author

    #     super(Profile, self).save(*args, **kwargs)


class ReplyComment(BaseComment):
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)
