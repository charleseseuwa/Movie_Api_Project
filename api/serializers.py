from rest_framework import serializers
from content.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"