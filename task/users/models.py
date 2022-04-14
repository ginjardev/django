from unicodedata import name
from django.contrib.auth.models import User
from django.db import models
from django.views.generic.dates import DayMixin
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=False),
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=14)
    allergies = models.BooleanField()
    food_diet = models.CharField(max_length=100)

class Allergens(models.Model):
    name = models.CharField(max_length=90)

class Meal(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=250)
    serving_size = models.IntegerField()
    allergens = models.ManyToManyField(Allergens)


class Order(models.Model):
    order_id = models.IntegerField(unique=True, auto_created=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    is_takeaway = models.BooleanField()


class Menu(Meal, DayMixin):
    food_list = []
    day_of_the_week = models.DateField()
    meal_time = models.CharField(max_length=50, blank=False)
