from django.urls import path
from . import views


app_name = "postapp"
urlpatterns = [   
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
    path('likes-by-user/<int:user_id>/', views.ordered_articles_by_likes)
    ]
