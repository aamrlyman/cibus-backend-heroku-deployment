from django.db import models

from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    notes = models.CharField(max_length=1000, blank=True, default= '')
    url = models.CharField(max_length=150, blank=True, default= '')
    prep_time_minutes = models.IntegerField(blank=True, default = 0)
    prep_time_hours = models.IntegerField(blank=True, default = 0)
    cook_time_minutes = models.IntegerField(blank=True, default = 0)
    cook_time_hours = models.IntegerField(blank=True, default = 0)


# Create your models here.
