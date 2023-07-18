from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import api_list_movies, movies_update, api_create_movies, get_external_movies

schema_view = get_schema_view(
   openapi.Info(
      title="CAPSTONE PROJECT MOVIE API",
      default_version='v1',
      description="Movie API Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path("api/", api_list_movies.as_view(), name= "home" ),
   path('create/', api_create_movies.as_view(), name="create"),
   path('external/', get_external_movies, name='external_api'),
   path("<int:id>/", movies_update.as_view(), name= "detail"),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
