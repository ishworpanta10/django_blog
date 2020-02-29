from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'text']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    context_object_name = 'details_doc'
    success_url = reverse_lazy('home')
