from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'details_doc'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'


class ArticleAllView(ListView):
    model = Article
    template_name = 'news.html'
