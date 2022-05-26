import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")

import django
django.setup()

from movies.models import Movie, Genre


def get_genre_data():
    genre_dict = {
        28: '액션',
        12: '모험',
        16: '애니메이션',
        35: '코미디',
        80: '범죄',
        99: '다큐멘터리',
        18: '드라마',
        10751: '가족',
        14: '판타지',
        36: '역사',
        27: '공포',
        10402: '음악',
        9648: '미스테리',
        10749: '로맨스',
        878: 'SF',
        10770: 'TV 영화',
        53: '스릴러',
        10752: '전쟁',
        37: '서부'
    }
    return genre_dict


def parse_movie_data():
    API_KEY = "bd2e2aed22ef7bc837f34ff1cf7ef434"
    BASE_URL = 'https://api.themoviedb.org/3/movie'
    POPULAR_URL = "/popular"
    result = {'movies': []}
    for page in range(1, 10):
        params = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': page
        }

        result['movies'].extend(requests.get(BASE_URL + POPULAR_URL, params=params).json().get('results'))

    return result


if __name__ == '__main__':
    movies = parse_movie_data().get('movies')
    genres = get_genre_data()

    for genre_id, name in genres.items():
        Genre(id=genre_id, name=name).save()

    for movie in movies:
        movie_id = movie.get('id')
        title = movie.get('title')
        original_language = movie.get('original_language')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        vote_average = movie.get('vote_average')
        poster_path = movie.get('poster_path')
        movie_genres = movie.get('genre_ids')

        if id and title and overview and poster_path:
            saved_movie = Movie(id=movie_id, title=title, original_language=original_language, overview=overview, release_date = release_date, vote_average=vote_average, poster_path=poster_path)
            saved_movie.save()
            
            for genre_id in movie_genres:
                saved_movie.genres.add(genre_id)
                print(genre_id)
        else:
            print(movie_id, title)