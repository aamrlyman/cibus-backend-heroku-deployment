from django.urls import path, include
from meal_schedules import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.get_create_Schedules),
    path('<int:schedule_id>/', views.schedule_detail),
    path('scheduled_meal/<int:scheduled_meal_id>/', views.scheduled_meal_detail),
   
    # path('<int:meal_id>/', views.meals_detail),
    # path('edit/', views.meals_detail),
]
