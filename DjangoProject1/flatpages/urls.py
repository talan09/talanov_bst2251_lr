from django.urls import path
from . import views

app_name = 'flatpages'

urlpatterns = [
    path('', views.home, name='home'),
    path('/hello', views.home, name='home'),
]