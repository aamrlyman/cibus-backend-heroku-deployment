from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Schedule, Scheduled_Meal
from .serializers import ScheduleSerializer, Scheduled_MealSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_create_Schedules(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST': #create schedule for user
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET': #get user schedule(s)
        user_schedule = Schedule.objects.filter(user_id=request.user.id)
        serializer = ScheduleSerializer(user_schedule, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def schedule_detail(request,schedule_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")    
    user_schedule = Schedule.objects.filter(user_id=request.user.id)
    serializer1 = ScheduleSerializer(user_schedule, many=True)

    def user_id_check():
        for id_obj in serializer1.data: 
            if id_obj["id"] == schedule_id: # type: ignore
                return True
    if user_id_check() != True:
        return Response(status=status.HTTP_403_FORBIDDEN) 

    # if user_schedule.count(schedule_id) < 1: # type: ignore
    scheduled_meals = Scheduled_Meal.objects.filter(schedule_id=schedule_id)
    # if scheduled_meals[0].user.id != request.user.id: # type: ignore
    if request.method == 'POST': # add meal to scheduled_meal
        serializer = Scheduled_MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET': #get all the meals on a schedule (scheduled_meals) by scheduled id
        serializer = Scheduled_MealSerializer(scheduled_meals, many=True )
        return Response(serializer.data)
    
    if request.method == 'DELETE': 
        scheduled_meals.delete()    
        return Response(status = status.HTTP_204_NO_CONTENT)



@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def scheduled_meal_detail(request, scheduled_meal_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    
    scheduled_meal = get_object_or_404(Scheduled_Meal, id=scheduled_meal_id)
    
    if scheduled_meal.user.id != request.user.id: # type: ignore
        return Response(status=status.HTTP_403_FORBIDDEN) 
    
    if request.method == 'GET': #get scheduled_meal by scheduled meal id
        serializer = Scheduled_MealSerializer(scheduled_meal);
        return Response(serializer.data)
    if request.method == "PUT": #toggle is_Cooked 
        is_cooked = {'is_Cooked': not scheduled_meal.is_Cooked }
        serializer = Scheduled_MealSerializer(scheduled_meal, data=is_cooked, partial = True); #type: ignore
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
    if request.method == "DELETE": #remove meal from Scheduled_meals
             scheduled_meal.delete()
             return Response(status = status.HTTP_204_NO_CONTENT)



    
