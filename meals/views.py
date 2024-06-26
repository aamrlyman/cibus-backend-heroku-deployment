from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Meal
from .serializers import MealSerializer
from django.shortcuts import get_object_or_404
from meal_schedules.models import Scheduled_Meal
from meal_schedules.serializers import Scheduled_MealSerializer


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET']) #get all meals
@permission_classes([AllowAny])
def meal_list(request):
    meals = Meal.objects.all()
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def meals_list_authenticated(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST': #create meal
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET': #get meals for user
        meals = Meal.objects.all()
        user_meals = meals.filter(user_id=request.user.id)
        serializer = MealSerializer(user_meals, many=True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def meals_detail(request, meal_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    meal = get_object_or_404(Meal, id=meal_id)
    if request.method == 'GET': #get meal by id
        serializer = MealSerializer(meal);
        return Response(serializer.data)

    if meal.user.id != request.user.id: # type: ignore
        return Response(status=status.HTTP_403_FORBIDDEN)        
        
    if request.method == "PUT": #edit meal
        serializer = MealSerializer(meal, data=request.data);
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    if request.method == "DELETE":
        scheduled_meals = Scheduled_Meal.objects.filter(meal__id=meal_id)
        if (len(scheduled_meals)> 0 ): #check if meal is on a meal schedule before deleting
            return Response(status=status.HTTP_409_CONFLICT)
        else: 
            meal.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
