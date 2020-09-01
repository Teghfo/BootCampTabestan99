from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.views.generic import View, DetailView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required


from .models import Article, Author
from .forms import ArticlePostForm, CommentForm, SearchForm
from user_profile.models import Profile


class index_blog(View):
    def get(self, request):
        articles = Article.objects.filter(
            Q(is_published=True), Q(is_active=True))
        published_articles = articles[:10]
        latest_article = articles.order_by('-created_date')[:3]
        best_authors = Author.objects.all()[:5]
        search_form = SearchForm()
        return render(request, 'index_blog.html', {'articles': published_articles, 'latest': latest_article, 'best_authors': best_authors, 'search_form': search_form})

    def post(self, request):
        return HttpResponse('you can not use post method')


# class HomePageView(TemplateView):

#     template_name = "index_blog.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_articles'] = Article.objects.all()[:5]
#         context['best_authors'] = Author.objects.all()[:5]
#         return context


class SearchArticle(View):

    def get(self, request, *args, **kwargs):
        search_text = request.GET['q']
        result = Article.objects.filter(
            Q(title__icontains=search_text) |
            Q(text__icontains=search_text)
        ).distinct()
        return render(request, 'search_results.html', {'search_result': result})

    def post(self, request, *args, **kwargs):
        # form = SearchForm(request.POST)
        # search_text = form['search'].value()

        search_text = request.POST['search']
        result = Article.objects.filter(
            Q(title__icontains=search_text) |
            Q(text__icontains=search_text)
        ).distinct()
        return render(request, 'search_results.html', {'search_result': result})


class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    # add your data -----> context['your_key'] = your_val
    #     return context


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'
    form = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comment_set.all()
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        article = self.get_object()
        if form.is_valid():
            form.instance.article = article
            form.save()
        return redirect(reverse('detail-article', kwargs={'slug': article.slug}))


def author_get_or_create(user):
    profile = Profile.objects.filter(user=user)[0]
    author = profile.author
    # .author_set.all()[0]
    if author:
        return author
    else:
        return None


class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticlePostForm
    login_url = 'login'
    success_url = '/blog/index'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # add your data -----> context['your_key'] = your_val
    #     return context

    def form_valid(self, form):
        form.save()
        author = author_get_or_create(self.request.user)
        form.instance.author.add(author)
        return super().form_valid(form)


class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticlePostForm
    #success_url = '/thanks/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # add your data -----> context['your_key'] = your_val
    #     return context

    def form_valid(self, form):
        #form.instance.author = author_get_or_create(self.request.user)
        return super().form_valid(form)


class DeleteArticleView(DeleteView):
    model = Article
    #success_url = '/thanks/'
    #template_name = 'article_confirm_delete.html'


# @permission_required('user_profile.delete_profile', login_url='login')
def hello(request):
    user = request.user
    if user.has_perm('user_profile.ter_kesh'):
        print('teryaki badbakht!')
    if user.groups.filter(name='khal_ghezi'):
        print('be khal ghezi vaslam')
    if not user.has_perm('user_profile.delete_profile'):
        print('hi')
        return redirect(reverse('login'))
    return HttpResponse('<h1>hello</h1>')
