from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),
    path('venues/', views.venue_list, name='venue_list'),
    path('events/', views.event_list, name='event_list'),
    path('services/', views.service_list, name='service_list'),
]
