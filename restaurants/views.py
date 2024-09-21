from django.shortcuts import render
from django.views import generic
from .models import Restaurant

def index(request):
    return render(request, 'index.html')

class RestaurantList(generic.ListView):
    queryset = Restaurant.objects.all()
    template_name = "restaurants.html"
    context_object_name = "restaurants"

