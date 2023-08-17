from .models import Article, UserModel
from django.db.models import Count
from django.http import Http404


def sorted_articles(user_id):
    try:
        user = UserModel.objects.get(id=user_id)
        annotated_articles = Article.objects.annotate(prefer_topics=Count('topics', topics__users=user))

        sorted_articles = annotated_articles.order_by('-prefer_topics', '-created_date')

        return sorted_articles
    except UserModel.DoesNotExist:
        raise Http404('User does not exist')
