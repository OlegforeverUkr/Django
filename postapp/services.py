from .models import Article, UserModel


def sorted_articles(user_id):
    try:
        user = UserModel.objects.get(id=user_id)
        liked_articles = Article.objects.filter(likes=user)
        ordered_articles = liked_articles.order_by('-likes__count')
        articles_titles = [article.title_article for article in ordered_articles]

        return articles_titles

    except UserModel.DoesNotExist:
        defult_ordering = Article.objects.order_by('-likes__count')
        defult_articles = [article.title_article for article in defult_ordering]
        return defult_articles

    