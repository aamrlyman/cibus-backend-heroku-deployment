from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Meal_Ingredient
from .serializers import Meal_IngredientSerializer, GroceriesSerializer
from django.shortcuts import get_object_or_404
from meals.models import Meal
from meals.serializers import MealSerializer
from meal_schedules.models import Schedule, Scheduled_Meal
from meal_schedules.serializers import ScheduleSerializer, Scheduled_MealSerializer


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_ingredients_by_meal_id(request):


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def ingredient_list(request, meal_id):

    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    # meal_id = request.query_params.get('meal_id')
    
    if request.method == 'POST':
        serializer = Meal_IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        ingredients = Meal_Ingredient.objects.filter(meal_id = meal_id)
        serializer = Meal_IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)



@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def ingredient_detail(request, pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    ingredient = get_object_or_404(Meal_Ingredient, pk=pk)

    if request.method == 'GET':
        serializer = Meal_IngredientSerializer(ingredient);
        return Response(serializer.data)
    if ingredient.user.id != request.user.id: # type: ignore
        return Response(status=status.HTTP_403_FORBIDDEN) 
    elif request.method == "PUT":
        serializer = Meal_IngredientSerializer(ingredient, data=request.data);
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
             ingredient.delete()
             return Response(status = status.HTTP_204_NO_CONTENT)


    # get an array that has all the meal_ids using a for loop 
    # get ingredients by meal_id for each meal in the array w/loop and put those in an array
    # serialize the data and return it in a response 

@api_view(["GET"])
@permission_classes([AllowAny])
def grocery_list(request,schedule_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    schedule_id = schedule_id 
    scheduled_meals = Scheduled_Meal.objects.filter(schedule_id=schedule_id)
    meal_ids = [scheduled_meal.meal.id for scheduled_meal in scheduled_meals] #type: ignore
    ingredients = Meal_Ingredient.objects.filter(meal_id__in=meal_ids)
    serializer = GroceriesSerializer(ingredients, many=True)
    print (ingredients)
    return Response(serializer.data)
      
# for email in Email.objects.values_list('email', flat=True).distinct():
#     Email.objects.filter(pk__in=Email.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()