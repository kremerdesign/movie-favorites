from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    release_year = models.SmallIntegerField(null=True, blank=True)
    critic_rating = models.SmallIntegerField(null=True, blank=True)
    poster = models.URLField(null=True, blank=True)
    mpaa_rating = models.CharField(max_length=100, null=True, blank=True)
    runtime = models.SmallIntegerField(null=True, blank=True)
    audience_score = models.SmallIntegerField(null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    rt_id = models.IntegerField(null=True, blank=True)


    def __unicode__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=120)
    rt_id = models.IntegerField(null=True, blank=True)
    movie = models.ForeignKey(Movie, null=True, blank=True, related_name='movie')

    def __unicode__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=120)
    actor = models.ForeignKey(Actor, null=True, blank=True, related_name='actor')

    def __unicode__(self):
        return self.name
