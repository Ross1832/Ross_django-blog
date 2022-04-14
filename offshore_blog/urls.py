from django.urls import path, reverse
from django.views.generic import TemplateView

from . import views


app_name = 'offshore_blog'

urlpatterns = [
    # path('', views.ArticleList.as_view()),
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.ArticlePage.as_view(), name='page_article'),
    path('search', views.search_outcome, name='search_result'),
]
