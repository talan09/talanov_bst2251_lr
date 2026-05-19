from django.urls import path
from . import views
from lab3.articles.views import *
from lab4.blog.views import *
from lab5.views import *
app_name = 'flatpages'  

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.helloWold, name='hello'),
    path('archive/', archive, name='archive'),
    path('article/<article_id>', get_article, name='article'),
    path('article/create/post', create_post, name='articleCreate'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('helloworld_js/', views.js, name='helloworld'),
]