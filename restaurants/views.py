from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Restaurant

def index(request):
    return render(request, 'index.html')

class RestaurantList(generic.ListView):
    queryset = Restaurant.objects.all()
    template_name = "restaurants.html"
    context_object_name = "restaurants"

def restaurant_detail(request, pk):
    """
    Display an individual :model:`Restaurant`.

    **Context**

    ``restaurant``
        An instance of :model:`Restaurant`.

    **Template:**

    :template:`restaurants/restaurant_detail.html`
    """
    restaurant = get_object_or_404(Restaurant, pk=pk)
    
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})