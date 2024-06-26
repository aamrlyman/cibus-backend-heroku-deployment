from rest_framework import serializers
from .models import Meal

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'notes', 'url', 
        'prep_time_minutes', 'prep_time_hours', 
        'cook_time_minutes', 'cook_time_hours', 'user_id']
        depth = 1
    # user_id = serializers.IntegerField(write_only=True)
