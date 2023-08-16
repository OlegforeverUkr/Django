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
    path('<int:article_id>/', views.article_detail_view, name='article-id'),
    path('about/', views.about_view, name='about'),
    ]
