from django.urls import path

from . import views as views

app_name = 'movies'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('top/', views.TopMovieList.as_view(), name='top_movies'),
    path('genre/', views.GenreIndexView.as_view(), name='genre_home'),
    path('genre/<slug:slug>/', views.GenreMovieList.as_view(), name='movies_by_genre'),
    path('<int:pk>-<slug:slug>/', views.MovieDetail.as_view(), name='movie_detail'),
]
