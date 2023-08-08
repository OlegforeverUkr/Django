from .models import Article
from django.db.models import Count


def sorted_articles(user):
    annotated_articles = Article.objects.annotate(prefer_topics=Count('topics', topics__users=user))

    sorted_articles = annotated_articles.order_by('-prefer_topics', '-created_date')

    return sorted_articles
