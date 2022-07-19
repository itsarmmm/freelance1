from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

LOGIN_REDIRECT_URL = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^signup/$', views.signup, name='signup'),
    path('logout/', views.pagelogout, name='user_logout'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('projects/', views.projects, name='projects'),
    path('profile/', views.profile, name='user_profile'),
    path('profile_edit/', views.profile_edit, name='user_profile_edit'),
    path('add_service/', views.add_service, name='add_service'),
]
