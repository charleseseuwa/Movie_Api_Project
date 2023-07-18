from django.db import models

# Create your models here.
RATINGS = (
    ('5', '5 star'),
    ('4', '4 star'),
    ('3', '3 star'),
    ('2', '2 star'),
    ('1', '1 star')
)

CHOICES = (
    ('action', 'Action'),
    ('drama', 'Drama'),
    ('romance', 'Romance'),
    ('epic', 'Epic')
)


class Movies(models.Model):
    title = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    category = models.CharField(choices=CHOICES, max_length=100)
    ratings = models.CharField(choices= RATINGS, max_length=100)
    date_released = models.DateField()
    duration = models.CharField(max_length=100)
    
    class Meta:
            verbose_name = "Movies"
            verbose_name_plural = "Movies"
            ordering = ['id']
        
    def __str__(self):
            return self.title
