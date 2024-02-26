from django.db import models

# Create your models here.
class Location(models.Model):
    ICAO_code = models.CharField(max_length=4, null=False, blank=False, primary_key=True)
    IATA_code = models.CharField(max_length=3, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    fromCity = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='departing_city')
    toCity = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='arrival_city')
    STD = models.DateTimeField(null=False) #Scheduled time departure
    ATD = models.DateTimeField(null=True) #Actual time departure
    STA = models.DateTimeField(null=False) #Scheduled time arrival
    ATA = models.DateTimeField(null=True) #Actual time arrival
    airliner = models.CharField(max_length=20, null=False, blank=False)

class Users(models.Model):
    username = models.CharField(max_length=35, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    userFlight = models.ForeignKey(Flight, on_delete=models.DO_NOTHING, null=True, blank=True)