from users.models import User
from movies.models import Movie, Genre

user = User.objects.get(id=1)
genres_list = Genre.objects.filter(id__in=user.genres.all())
genres_count = genres_list.count()
all_movies = Movie.objects.filter(genres__in=genres_list)
movies_list = []
for movie in all_movies:
    if movie not in movies_list:
        movies_list.append(movie)


movie_count = len(movies_list)

