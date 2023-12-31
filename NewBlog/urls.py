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
    path('hello/', views.hello_view),
    path('', views.empty_view),
    path('<article>/comment/', views.article_comment),
    path('create/', views.article_create_view),
    path('<article>/update/', views.article_update_view),
    path('<article>/delete/', views.article_delete_view),
    path('topics/', views.topics),
    path('topics/<topic>/subscribe/', views.topics_subscribe),
    path('topics/<topic>/unsubscribe/', views.topics_unsubscribe),
    path('profile/<str:username>/', views.profile_user),
    path('set-password/', views.set_password),
    path('set-userdata/', views.set_userdata),
    path('deactivate/', views.deactivate),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('<int:article_id>/', views.article_detail_view),
    path('likes-by-user/<int:user_id>/', views.ordered_articles_by_likes),
]
