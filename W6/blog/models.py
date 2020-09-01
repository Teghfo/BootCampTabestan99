from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from django.urls import reverse

from user_profile.models import Profile


class Author(models.Model):
    profile = models.OneToOneField(
        Profile, related_name='author', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.full_name

    def update_rate(self, new_rate):

        self.rate = new_rate


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(unique=True, allow_unicode=True)
    poster = models.ImageField(upload_to='blog/images/')
    author = models.ManyToManyField(Author)
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True, blank=True)
    rate_article = models.FloatField(default=0)
    video = models.FileField(upload_to='blog/videos/', null=True, blank=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)[:100]
        super(Article, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("detail-article", kwargs={"slug": str(self.slug)})


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
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE_CHOICE, null=True, blank=True)
    is_show = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Comment(BaseComment):
    pass

    def save(self, *args, **kwargs):
        rate_count = self.article.comment_set.all().filter(rate__gt=0).count()
        if self.rate:
            new_rate = (((self.article.rate_article)*rate_count) +
                        self.rate) / (rate_count + 1)
            self.article.rate_article = new_rate
            self.article.save()
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ReplyComment(BaseComment):
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Koofti(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=10)
