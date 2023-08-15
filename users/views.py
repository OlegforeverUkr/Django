from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from postapp.models import Article, UserModel
from .forms import UserLoginForm, UserRegistrationForm
from postapp.services import sorted_articles
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse



def profile_user(request: HttpRequest, username: str) -> HttpResponse:

    try:
        user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        raise Http404('User does not exist')

    response = {
        'user': user,
    }

    return render(request, 'profile_user.html', response)


def user_page(request: HttpRequest, username: str) -> HttpResponse:
    try:
        user = UserModel.objects.get(username=username)
        articles = Article.objects.filter(author=user)
        articles_on_preferred_topics = sorted_articles(user.id)

    except UserModel.DoesNotExist:
        raise Http404('User does not exist')


    context = {
        'user': user.username,
        'articles_user': articles,
        'articles': articles_on_preferred_topics,
    }

    return render(request, 'config.html', context)



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

            url = reverse('users:login')
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
    url = reverse('users:login')
    return HttpResponseRedirect(url)
