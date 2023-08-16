from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path('profile/<str:username>/', views.profile_user, name='profile-user'),
    path('user-settings/<str:username>/', views.user_page, name='config'),
    path('set-password/', views.set_password, name='set-password'),
    path('set-userdata/', views.set_userdata, name='set-userdata'),
    path('deactivate/', views.deactivate, name='deactivate'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]