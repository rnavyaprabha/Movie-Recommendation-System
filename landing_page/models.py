from django.db import models
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    # Add any additional fields you need for your custom user model
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)
    
    # Define the ManyToManyField to establish the relationship with Genre
    favorite_genres = models.ManyToManyField(Genre)
    imdb = models.IntegerField(null=True)
    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Users'
        permissions = [('can_update_profile', 'Can Update Profile')]

# Specify custom related_names for the groups and user_permissions fields
User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'
# Create your models here.

class Movie(models.Model):
    poster = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    certificate = models.CharField(max_length=50, null=True)
    runtime = models.CharField(max_length=50, null=True)
    genre = models.ManyToManyField(Genre)
    imdb = models.FloatField(null=True)
    overview = models.TextField(null=True)
    meta_score = models.IntegerField(null=True)
    director = models.CharField(max_length=100, null=True)
    actor1 = models.CharField(max_length=100, null=True)
    actor2  = models.CharField(max_length=100, null=True)
    actor3 = models.CharField(max_length=100, null=True)
    actor4 = models.CharField(max_length=100, null=True)
    votes = models.IntegerField(null=True)
    gross = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title
