from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add =True)
    photo = models.CharField(max_length=2000, null=True, blank=True)