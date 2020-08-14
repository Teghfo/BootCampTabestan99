from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView

from .models import Article, Author


class index_blog(View):
    def get(self, request):

        return render(request, 'index_blog.html')

    def post(self, request):
        return HttpResponse('you can not use post method')


class HomePageView(TemplateView):

    template_name = "index_blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        context['best_authors'] = Author.objects.all()[:5]
        return context


class ArticleDetail(DetailView):

    model = Article
