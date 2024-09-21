from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
]