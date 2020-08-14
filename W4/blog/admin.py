from django.contrib import admin


from .models import Article, Author, ArticleImages


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'is_published',
              'poster', 'published_date', 'author')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(ArticleImages)
