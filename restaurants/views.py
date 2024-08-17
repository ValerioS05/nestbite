from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def my_restaurants(request):
    return HttpResponse("My first app")