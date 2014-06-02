from django.db import models

from django.core.urlresolvers import reverse

class Movie(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)
    short_description = models.CharField(max_length=500)
    fav_movies = models.CharField(max_length=500)
    fav_directors = models.CharField(max_length=500)
    fav_actors = models.CharField(max_length=500)
    fav_genres = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movies_edit', kwargs={'pk': self.pk})
