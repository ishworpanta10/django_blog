from django.urls import path

from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailsView.as_view(), name='article_page'),
    path('article/new_article/',
         views.ArticleCreateView.as_view(), name='article_new'),
    path('article/all_news/',
         views.ArticleAllView.as_view(), name='article_all'),
    path('article/<int:pk>/edit',
         views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete',
         views.ArticleDeleteView.as_view(), name='article_delete'),
]
