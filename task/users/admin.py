from django.contrib import admin
from .models import *
# Register your models here.
my_models = [UserProfile, Meal, Menu, Order]
admin.site.register(my_models)