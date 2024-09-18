from django.shortcuts import render
from django.views import generic
from .models import Restaurant
# Create your views here.


class RestaurantList(generic.ListView):
    queryset = Restaurant.objects.all()
    template_name = "restaurant_list.html"