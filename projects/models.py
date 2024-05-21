from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    homepage = models.URLField(blank=True)
    repo = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']