from django.db import models
from authentication.models import User
from meals.models import Meal
# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled_meals = models.ManyToManyField(Meal, through='Scheduled_Meal')

class Scheduled_Meal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_Cooked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#django.forms.CheckboxInput

# https://docs.djangoproject.com/en/4.1/topics/db/models/