import movie.models as mm
import scripts.city_alpha as sc
import scripts.districts as sd



def get_cover():
    cover = mm.Cover.objects.filter(is_alive=True)
    if cover:
        cover = cover[0].cover_img.url
    return cover


def get_movielist():
    movies = mm.Movie.objects.filter(is_in_theater=True).filter(is_top=False)
    top_movie = mm.Movie.objects.get(is_top=True)
    movie_list = [{'movie_id': i.id, 
                   'cover_me': i.poster_url_me,
                   'movie_name': i.name} for i in movies]
    top = {'movie_id': top_movie.id,
                 'cover_big': top_movie.poster_url_big,
                 'movie_name': top_movie.name,
                 'directors': top_movie.directors,
                 'casts': top_movie.casts,
                 'rating': top_movie.rating,
                 'genes': top_movie.genes,}
    return movie_list, top


def get_movie_info(movie_number):
    movies = mm.Movie.objects.filter(id=movie_number)
    movies = list(movies)[0]
    movie_info = {'name': movies.name,
                  'cover_big': movies.poster_url_big,
                  'directors': movies.directors,
                  'casts': movies.casts,
                  'rating': movies.rating,
                  'genes': movies.genes,}
    return movie_info
    

def get_cinema_address(city, area):
    cinemas = mm.CinemaUrl.objects.filter(city__contains=city, district__startswith=area)
    results = []
    for cinema in cinemas:
        result = {'cinema_name': '',
                  'source': 'ALL',
                  'cinema_id': 0,}
        result['cinema_name'] = cinema.cinema_name
        result['cinema_id'] = cinema.id
        result['source'] = get_cinemadata_source(cinema)
        results.append(result)
    return results


def get_cinemadata_source(cine):
    source = 'ALL'
    if cine.taopp_url and cine.nuomi_url and cine.time_url:
        source = 'ALL'
    elif cine.taopp_url and cine.nuomi_url:
        source = '淘|糯'
    elif cine.taopp_url and cine.time_url:
        source = '淘|时'
    elif cine.nuomi_url and cine.time_url:
        source = '糯|时'
    elif cine.nuomi_url:
        source = '糯'
    elif cine.time_url:
        source = '时'
    elif cine.taopp_url:
        source = '淘'
    return source
    

def get_all_city():
    results = sc.city
    return results


def get_district(city_name):
    results = sd.dct[city_name] 
    return results
