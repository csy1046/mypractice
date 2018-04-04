from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404

import movie.handlers as mh


# Create your views here.


def index(request):

    return render(request, 'index.html', {})

def movie_info(request):
 
    return render(request, 'movieinfo.html', {})

def get_current_movie_list(request):
    cover = mh.get_cover()
    movie_list, top_movie = mh.get_movielist()
    content = {
        'cover': cover,
        'movies': movie_list,
        'top': top_movie
    }
    return JsonResponse(content)

def get_movie_infodata(request):
    movie_number = request.GET.get('movie_number', None)
    if movie_number:
        movie_info = mh.get_movie_info(movie_number)
        return JsonResponse(movie_info)
    else:
        raise Http404


def get_cinema_address(request):
    city = request.POST.get('city', None)
    district = request.POST.get('district', None)
    if not city and not district:
        raise Http404
    result = mh.get_cinema_address(city, district)
    return JsonResponse({'result': result})

def get_all_city(request):
    results = mh.get_all_city()
    return JsonResponse(results)


def get_districtinfo(request):
    city_name = request.GET.get('city_name', None)
    if not city_name:
        raise Http404
    results = mh.get_district(city_name)
    return JsonResponse({'result': results})

def get_movie_tickets(request):
    return 0 
