from rest_framework import serializers
from .models import Schedule, Scheduled_Meal

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'user_id']
        depth = 1
    user_id = serializers.IntegerField(write_only=True)
    # scheduled_meals = serializers.IntegerField(write_only=True)


class Scheduled_MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduled_Meal
        fields = ['id', 'is_Cooked', 'meal_id', 'schedule_id', 'user_id', 'meal']
        depth = 1
    meal_id = serializers.IntegerField(write_only=True)
    schedule_id = serializers.IntegerField(write_only=True)
    # user_id = serializers.IntegerField(write_only=True)
    # user_id = serializers.IntegerField(write_only=True)
