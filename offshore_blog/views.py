from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from . import form
from .models import Article, Comment

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView


# class ArticleList(ListView):
#     model = Article
#     template_name = 'offshore_blog/index.html'
#     paginate_by = 3
#     context_object_name = "articles"
#
#     def get_queryset(self):
#         return Article.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         context['article_views'] = Article.objects.top_articles()
#         context['5_last_comments'] = Comment.objects.last_5_comments()
#         return context


def index(request):
    """This view function returns html text for articles list"""
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'articles': Article.objects.all(),
        'article_views': Article.objects.top_articles(),
        '5_last_comments': Comment.objects.last_5_comments(),
    }
    return render(request, 'offshore_blog/index.html', context)


class ArticlePage(FormView):
    template_name = 'offshore_blog/article.html'
    form_class = form.CommentForm
    success_url = ''

    def get_context_data(self, **kwargs):

        comment_form = form.CommentForm()

        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs['article_id'])
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['article_id'])
        context['article_views'] = Article.objects.top_articles()
        context['5_last_comments'] = Comment.objects.last_5_comments()
        context['comment_form'] = comment_form

        if self.request.method == "GET":
            context['article'].increment()
        elif self.request.method == "POST":
            comment_form = form.CommentForm(self.request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                user_comment.post = context['article']
                user_comment.save()
                return HttpResponseRedirect(reverse('page_article', args=[context['article']]))
        return context



# def page_article(request, article_id):
#     """This view function returns html text for particular article"""
#     article = get_object_or_404(Article, pk=article_id)
#     comments = Comment.objects.filter(post_id=article_id)
#     # comment = Comment.objects.
#     # old solution
#     # Article.objects.filter(pk=article_id).update(page_views=F('page_views') + 1)
#     # article_views = Article.objects.order_by('-page_views')[:5]
#     # old solution
#     comment_form = form.CommentForm()
#     """increment article views counter"""
#     if request.method == "GET":
#         article.increment()
#     elif request.method == "POST":
#         comment_form = form.CommentForm(request.POST)
#         if comment_form.is_valid():
#             user_comment = comment_form.save(commit=False)
#             user_comment.post = article
#             user_comment.save()
#             return HttpResponseRedirect(reverse('page_article', args=[article_id]))
#
#     # prepare view context
#     context = {
#         'article': article,
#         'article_views': Article.objects.top_articles(),
#         'comments': comments,
#         '5_last_comments': Comment.objects.last_5_comments(),
#         'comment_form': comment_form,
#     }
#     return render(request, 'offshore_blog/article.html', context)


def search_outcome(request):
    context = {
        'article_views': Article.objects.top_articles(),
        '5_last_comments': Comment.objects.last_5_comments(),
    }
    return render(request, 'offshore_blog/search_result.html', context)
