from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from .models import  Article, Comment, UserModel, Topic
from .forms import UserLoginForm, UserRegistrationForm
from .services import sorted_articles
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


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

    response = {
        'article_single': article_single,
        'article_title': article_single.title_article,
        'article_text': article_single.text_article,
        'article_author':article_single.author,
        'article_create': article_single.created_date,
        'article_topics': article_single.topics,
        'comments': comments
    }

    return render(request, 'article_detail.html', response)


def article_comment(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Comment to article - {article}')


def article_create_view(request: HttpRequest) -> HttpResponse:    
    return render(request, 'create.html')


def article_update_view(request: HttpRequest, article_id: int) -> HttpResponse:
    try:
        article_single = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    response = {
        'article_single': article_single,
        'article_text': article_single.text_article,
        'article_title': article_single.title_article}
    return render(request, 'update_art.html', response)


def article_delete_view(request: HttpRequest, article_id: int) -> HttpResponse:
    try:
        article_single = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    response = {
        'article_title': article_single.title_article}
    return render(request, 'delete.html', response)


def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page with topics')


def topics_subscribe(request: HttpRequest, topic: str) -> HttpResponse:
    try:
        cur_topic = Topic.objects.get(topic_name=topic)
        related_articles = Article.objects.filter(topics=cur_topic)
        response = {'topic': cur_topic, 'related_articles': related_articles}
        return render(request, 'subscribe_topic.html', response)
    except Topic.DoesNotExist:
        raise Http404('Topic does not exist.')


def topics_unsubscribe(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f'Unsubscribe on topic - {topic}')


def profile_user(request: HttpRequest, username: str) -> HttpResponse:

    try:
        user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        raise Http404('User does not exist')

    response = {
        'user': user,
    }

    return render(request, 'profile_user.html', response)


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page set password')


def set_userdata(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page userdata')


def deactivate(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page deactivate')



def register(request: HttpRequest) -> HttpResponse:
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.create_user()

            url = reverse('postapp:login')
            return HttpResponseRedirect(url)
    else:
        form = UserRegistrationForm()

    return render(request, 'register_page.html', {'form':form})


@require_http_methods(['POST', 'GET'])
def login_user(request: HttpRequest) -> HttpResponse:

    if request.method =='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            login(request, user)

            url = reverse('postapp:home-page')
            return HttpResponseRedirect(url)

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form':form})


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    url = reverse('postapp:login')
    return HttpResponseRedirect(url)


def ordered_articles_by_likes(user_id: int):
    try:
        user = UserModel.objects.get(id=user_id)
        articles = sorted_articles(user_id)
        return articles
    except UserModel.DoesNotExist:
        raise Http404('User does not exist')

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def config(request: HttpRequest, username: str) -> HttpResponse:
    try:
        user = UserModel.objects.get(username=username)
        articles = Article.objects.filter(author=user)
        articles_on_preferred_topics = ordered_articles_by_likes(user.id)

    except UserModel.DoesNotExist:
        raise Http404('User does not exist')


    response = {
        'user': user.username,
        'articles_user': articles,
        'articles': articles_on_preferred_topics,
    }

    return render(request, 'config.html', response)


    
