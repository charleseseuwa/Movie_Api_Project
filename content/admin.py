from django.contrib import admin
from .models import Movies

# Register your models here.
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'actors', 'category', 'date_released']