from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField(blank=True, unique=True)
