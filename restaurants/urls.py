from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('restaurants/', views.RestaurantList.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
]