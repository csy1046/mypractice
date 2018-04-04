from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movieinfo$', views.movie_info, name='movie-info'),
    url(r'^currentmovielist', views.get_current_movie_list, name='get-current-movie-list'),
    url(r'^movieinfodata$', views.get_movie_infodata, name='get-movie-infodata'),
    url(r'^cinemaadd$', views.get_cinema_address, name='get-cinema-address'),
    url(r'^cityinfo$', views.get_all_city, name='get-all-city'),
    url(r'^districtinfo$', views.get_districtinfo, name='get-districtinfo'),
    url(r'^tickets$', views.get_movie_tickets, name='get-movie-tickets')
]
