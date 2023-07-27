"""
URL configuration for NewBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.func_hello),
    path('', views.func_empty),
    path('<article>/', views.func_article),
    path('<article>/comment/', views.func_comment),
    path('create/', views.func_create),
    path('<article>/update/', views.func_article_update),
    path('<article>/delete/', views.func_article_delete),
    path('topics/', views.func_topics),
    path('topics/<topic>/subscribe/', views.func_topics_subscribe),
    path('topics/<topic>/unsubscribe/', views.func_topics_unsubscribe),
    path('profile/<str:username>/', views.func_profile),
    path('set-password/', views.func_set_password),
    path('set-userdata/', views.func_set_userdata),
    path('deactivate/', views.func_deactivate),
    path('register/', views.func_register),
    path('login/', views.func_login),
    path('logout/', views.func_logout),
]
