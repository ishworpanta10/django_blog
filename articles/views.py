from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'details.html'
    context_object_name = 'details_doc'
