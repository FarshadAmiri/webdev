from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} {self.city}"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name='departure', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return f'Flight_id: {self.id} | {self.origin} to {self.destination} ({self.duration} minutes)'

class Passenger(models.Model):
    nick = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    flights = models.ManyToManyField(Flight, blank= True, related_name='passengers')

    def __str__(self):
        return f'{self.nick} {self.last}'