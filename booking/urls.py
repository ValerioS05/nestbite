from . import views
from django.urls import path


urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('create/<int:restaurant_id>/', views.create_booking, name='create_booking'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('<int:booking_id>/update/', views.update_booking, name='update_booking'),
]