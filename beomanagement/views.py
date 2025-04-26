from django.shortcuts import render
from .models import Client, Venue, Event, Service

def home(request):
    return render(request, 'beomanagement/home.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'beomanagement/client_list.html', {'clients': clients})

def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'beomanagement/venue_list.html', {'venues': venues})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'beomanagement/event_list.html', {'events': events})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'beomanagement/service_list.html', {'services': services})
