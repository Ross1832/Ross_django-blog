from django.db import models
from django.db.models import F
from mptt.models import MPTTModel, TreeForeignKey


class ArticleManager(models.Manager):
    @staticmethod
    def top_articles(limit=5):
        return Article.objects.order_by('-page_views')[:limit]


class CommentManager(models.Manager):
    @staticmethod
    def last_5_comments(limit=5):
        return Comment.objects.order_by('-pub_date')[:limit]


class Article(models.Model):
    head_article = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    page_views = models.IntegerField(default=0)
    objects = ArticleManager()

    def increment(self):
        Article.objects.filter(id=self.pk).update(page_views=F('page_views') + 1)

    def __str__(self):
        return self.head_article

    def get_absolute_url(self):
        return u'' % self.id


class Comment(MPTTModel):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    objects = CommentManager()

    class MPTTMeta:
        order_insertion_by = ['pub_date']

    def __str__(self):
        return self.content
