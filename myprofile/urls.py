from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('contact/', views.contact_us, name='contact_us'),
]
