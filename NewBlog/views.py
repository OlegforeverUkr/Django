from django.http import HttpRequest, HttpResponse


def func_hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello Page')


def func_empty(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Empty Page')


def article_detail_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Page from article - {article}')


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
    return HttpResponse(f'Profile - {username}')


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
