from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('movie_list', views.movie_list, name='movie list'),
    path('movie_detail', views.movie_detail, name='movie detail'),
    path('attend', views.attend, name='attend'),
    path('attend_summary', views.attend_summary, name='attend_summary'),
]