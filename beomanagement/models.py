from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    name     = models.CharField(max_length=200)
    address  = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate'),
        ('birthday', 'Birthday'),
        ('conference', 'Conference'),
    ]
    
    event_name  = models.CharField(max_length=200)
    event_date  = models.DateField()
    event_type  = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    client      = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="events")
    venue       = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.event_name} - {self.event_date}"


class Service(models.Model):
    event       = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="services")
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost        = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
