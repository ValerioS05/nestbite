from django.shortcuts import render, get_object_or_404
from django.views import generic
from datetime import datetime
from .models import Restaurant

def index(request):
    """ Renders the homepage view (index). """
    return render(request, 'index.html')


class RestaurantList(generic.ListView):
    template_name = "restaurants.html"
    context_object_name = "restaurants"
    paginate_by = 3

    def get_queryset(self):
        return restaurant_filter(self.request)


def restaurant_filter(request):
    """
    Filters restaurants based on capacity and opening time.

    Args:
        request (HttpRequest): The HTTP request containing GET params
        capacity/opening_time.

    Returns:
        A filtered queryset of Restaurant objects.
    """
    queryset = Restaurant.objects.all()

    capacity = request.GET.get('capacity')
    opening_time_str = request.GET.get('opening_time')
    opening_time = datetime.strptime(
        opening_time_str, '%H:%M').time() if opening_time_str else None

    if capacity:
        queryset = queryset.filter(capacity__gte=capacity)

    if opening_time:
        queryset = queryset.filter(
            opening_time__lte=opening_time, closing_time__gte=opening_time)

    return queryset


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(
        request, 'restaurant_detail.html', {'restaurant': restaurant})
