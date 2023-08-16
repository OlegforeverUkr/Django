from django.http import HttpRequest, HttpResponse, Http404
from .models import  Article, Comment, UserModel, Topic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def empty_view(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    user = request.user

    return render(request, 'article_list.html', {'articles': articles, 'user': user})


def article_detail_view(request: HttpRequest, article_id: int) -> HttpResponse:

    try:
        article_single = Article.objects.get(id=article_id)
        comments = Comment.objects.filter(article=article_single)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    context = {
        'article_single': article_single,
        'comments': comments
    }

    return render(request, 'article_detail.html', context)


def article_comment(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Comment to article - {article}')


def article_create_view(request: HttpRequest) -> HttpResponse:    
    return render(request, 'create.html')


def article_update_view(request: HttpRequest, article_id: int) -> HttpResponse:
    try:
        article_single = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    context = {
        'article_single': article_single}
    return render(request, 'update_art.html', context)


def article_delete_view(request: HttpRequest, article_id: int) -> HttpResponse:
    try:
        article_single = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    context = {
        'article_title': article_single.title_article}
    return render(request, 'delete.html', context)


def topics(request: HttpRequest) -> HttpResponse:
    all_topics = Topic.objects.all()
    all_articles = Article.objects.all()
    context = {'all_topics': all_topics,
               'all_articles': all_articles}
    return render(request, 'all_topics.html', context)


def topics_unsubscribe(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f'Unsubscribe on topic - {topic}')


def topics_subscribe(request: HttpRequest, topic: str) -> HttpResponse:
    try:
        cur_topic = Topic.objects.get(topic_name=topic)
        related_articles = Article.objects.filter(topics=cur_topic)
        context = {'topic': cur_topic, 'related_articles': related_articles}
        return render(request, 'subscribe_topic.html', context)
    except Topic.DoesNotExist:
        raise Http404('Topic does not exist.')

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')