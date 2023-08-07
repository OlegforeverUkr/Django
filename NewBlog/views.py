from django.http import HttpRequest, HttpResponse, Http404
from postapp.models import  Article, Comment, UserModel
from postapp.services import sorted_articles


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello Page')


def empty_view(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return HttpResponse(''.join(article.title for article in articles))


def article_detail_view(request: HttpRequest, article: str) -> HttpResponse:

    try:
        article_single = Article.objects.get(id=article)
        comments = Comment.objects.filter(article=article_single)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')
    except Article.MultipleObjectsReturned:
        raise Http404('More than one article on this id')

    comments_text = [comment.text_comment for comment in comments]

    response = {
        'article': [article_single.title_article,
                    article_single.text_article],
        'comments': comments_text
    }

    return HttpResponse(response)


def article_comment(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Comment to article - {article}')


def article_create_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Create Page')


def article_update_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Update to article - {article}')


def article_delete_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Delete to article - {article}')


def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page with topics')


def topics_subscribe(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f'Subscribe on topic - {topic}')


def topics_unsubscribe(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f'Unsubscribe on topic - {topic}')


def profile_user(request: HttpRequest, username: str) -> HttpResponse:

    try:
        user = UserModel.objects.get(username=username)
        articles = Article.objects.filter(author=user)
    except UserModel.DoesNotExist:
        raise Http404('User does not exist')
    except UserModel.MultipleObjectsReturned:
        raise Http404('More than one user on this username')

    articles_list = [article.title_article for article in articles]

    response = {
        'user': user.username,
        'articles': articles_list
    }

    return HttpResponse(response)


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page set password')


def set_userdata(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page userdata')


def deactivate(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page deactivate')


def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page register')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page login')


def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page logout')


def ordered_articles_by_likes(request: HttpRequest, user_id: int) -> HttpResponse:
    articles = sorted_articles(user_id)
    if articles is None:
        raise Http404('User with this id is not found')
    return articles
    

