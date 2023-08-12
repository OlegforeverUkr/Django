from django.urls import path
from . import views


app_name = "postapp"
urlpatterns = [
    path('', views.empty_view, name='home-page'),
    path('<article>/comment/', views.article_comment, name='article-comment'),
    path('create/', views.article_create_view, name='create'),
    path('<int:article_id>/update/', views.article_update_view, name='article-update'),
    path('<int:article_id>/delete/', views.article_delete_view, name='article-delete'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic>/subscribe/', views.topics_subscribe, name='topic-subscribe'),
    path('topics/<topic>/unsubscribe/', views.topics_unsubscribe, name='topic-unsubscribe'),
    path('profile/<str:username>/', views.profile_user, name='profile-user'),
    path('set-password/', views.set_password, name='set-password'),
    path('set-userdata/', views.set_userdata, name='set-userdata'),
    path('deactivate/', views.deactivate, name='deactivate'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:article_id>/', views.article_detail_view, name='article-id'),
    path('likes-by-user/<int:user_id>/', views.ordered_articles_by_likes, name='likes-by-user'),
    path('about/', views.about_view, name='about'),
    path('cofig/<str:username>/', views.config, name='config'),
    ]
