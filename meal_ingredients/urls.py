from django.urls import path, include
from meal_ingredients import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('meal_id/<int:meal_id>/', views.ingredient_list),
    path('<int:pk>/', views.ingredient_detail),
    path('grocery_list/<int:schedule_id>/', views.grocery_list),
]
