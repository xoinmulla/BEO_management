from django.contrib import admin
from .models import Client, Venue, Event, Service

admin.site.register(Client)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Service)
