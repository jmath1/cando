from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=140, default="")
    body = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='static/blog_images')