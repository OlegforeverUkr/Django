from django.http import HttpRequest, HttpResponse


def func_hello(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello Page')


def func_empty(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Empty Page')


def func_article(response: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Page from article - {article}')


def func_comment(response: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Comment to article - {article}')


def func_create(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Create Page')


def func_article_update(response: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Update to article - {article}')


def func_article_delete(response: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f'Delete to article - {article}')


def func_topics(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page with topics')


def func_topics_subscribe(response: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f'Subscribe on topic - {topic}')


def func_topics_unsubscribe(response: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f'Unsubscribe on topic - {topic}')


def func_profile(response: HttpRequest, username: str) -> HttpResponse:
    return HttpResponse(f'Profile - {username}')


def func_set_password(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page set password')


def func_set_userdata(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page userdata')


def func_deactivate(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page deactivate')


def func_register(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page register')


def func_login(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page login')


def func_logout(response: HttpRequest) -> HttpResponse:
    return HttpResponse('Page logout')
