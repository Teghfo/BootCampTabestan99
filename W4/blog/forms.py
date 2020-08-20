from django import forms

from .models import Article, Comment


class ArticlePostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'poster')


class CommentForm(forms.ModelForm):
    # rate = forms.IntegerField()

    class Meta:
        model = Comment
        fields = ('name', 'content', 'rate')


class SearchForm(forms.Form):
    search = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={'size': '40'}))
