from .models import Article, UserModel


def sorted_articles(user_id):
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return None

    liked_articles = Article.objects.filter(likes=user)
    ordered_articles = liked_articles.order_by('-likes__count')
    articles_titles = [article.title_article for article in ordered_articles]

    return articles_titles