from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('<int:article_id>/', views.show, name='show'),
    path('create/', views.create_post, name='create'),
    path('', views.index, name='index')

]