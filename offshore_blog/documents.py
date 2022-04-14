from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Article


@registry.register_document
class ArticleDocument(Document):
    class Index:
        name = "article"

    class Django:
        model = Article

        fields = ['content',
                  ]
