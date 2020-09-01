from django.contrib import admin


from .models import Article, Author, ArticleImages, Comment, Koofti


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'is_published',
              'poster', 'published_date', 'is_active', 'author')

    list_display = ('title', 'slug',  'rate_article')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(ArticleImages)
admin.site.register(Comment)
admin.site.register(Koofti)
