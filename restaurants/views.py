from django.shortcuts import render, get_object_or_404
from django.views import generic
from datetime import datetime
from .models import Restaurant


def index(request):
    return render(request, 'index.html')


class RestaurantList(generic.ListView):
    template_name = "restaurants.html"
    context_object_name = "restaurants"

    def get_queryset(self):
        return restaurant_filter(self.request)


def restaurant_filter(request):
    # Start with all restaurants
    queryset = Restaurant.objects.all()

    # Get filter parameters from the request
    capacity = request.GET.get('capacity')
    opening_time_str = request.GET.get('opening_time')

    # Convert opening time string to a time object
    opening_time = datetime.strptime(
        opening_time_str, '%H:%M').time() if opening_time_str else None

    # Apply capacity filter if provided
    if capacity:
        queryset = queryset.filter(capacity__gte=capacity)

    # Apply opening time filter if provided
    if opening_time:
        # Filter restaurants that are open at the specified opening time
        queryset = queryset.filter(
            opening_time__lte=opening_time, closing_time__gte=opening_time)

    return queryset


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(
        request, 'restaurant_detail.html', {'restaurant': restaurant})
