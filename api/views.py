from django.shortcuts import render
from rest_framework.response import Response
import requests
from pprint import pprint
from rest_framework.authtoken.models import Token
from content.models import Movies
from .serializers import MoviesSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter
from rest_framework import status 
import requests
from utils import get_movie_data
from django.http import HttpResponse
# Create your views here.

class api_list_movies(ListAPIView):
    queryset = Movies.objects.all().reverse()
    serializer_class = MoviesSerializer
    pagination_class = PageNumberPagination 
    filter_backends = [SearchFilter] 
    search_fields = ["title", "actors", "category"]
    
class api_create_movies(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class movies_update(RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    lookup_field = "id"
    
# class external_api_movies(generics.GenericAPIView):
#     api_key = '66986fa338a04d3c261db19dd555ab93'
#     response = requests.get("https://api.themoviedb.org/3/movie/popular", 
#                         params={'api_key':api_key,
#                                 })
    
#     pprint(response.json())


def get_external_movies(request):
    url = "https://api.themoviedb.org/3/movie/popular"
    movies = get_movie_data(url)
    for i in range(5):
        title = movies["results"][i]["title"]
        date_released = movies["results"][i]["release_date"]
        ratings = int(movies["results"][i]["vote_average"])

        if ratings > 5:
            ratings = 5
        
        Movies.objects.create(title=title, date_released=date_released, ratings=ratings)

    print(title, date_released, ratings)
    return HttpResponse("Movies have been added")


    
