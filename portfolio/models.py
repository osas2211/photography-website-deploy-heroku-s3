from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class home_page(models.Model):
    images = models.ImageField(upload_to = 'media/photos', null = True)
    date_posted = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return f'photo-{timezone.now()}'
    
    class Meta:
        ordering = ["-date_posted"]



class showcase(models.Model):
    heading = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'showcase'

class about(models.Model):
    name = models.CharField(max_length=150, null=True)
    about_me = models.TextField(null=True)
    title = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to = 'media/about_me', null=True)
    top_text = models.TextField(max_length=300, null=True)

    def __str__(self):
        return 'About'
    




