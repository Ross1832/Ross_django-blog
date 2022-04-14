from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Article, Comment

# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, MPTTModelAdmin)
