from django.db import models
from authentication.models import User
from meals.models import Meal

class Meal_Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    unit = models.CharField(max_length=30, blank=True, default= '')
    quantity = models.IntegerField(blank=True, default = 0 )

# Create your models here.
