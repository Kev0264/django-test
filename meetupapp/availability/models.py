from django.db import models
from django.contrib.auth.models import User

class GeneralAvailability(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monday = models.CharField(max_length=100, blank=True)
    tuesday = models.CharField(max_length=100, blank=True)
    wednesday = models.CharField(max_length=100, blank=True)
    thursday = models.CharField(max_length=100, blank=True)
    friday = models.CharField(max_length=100, blank=True)
    saturday = models.CharField(max_length=100, blank=True)
    sunday = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s General Availability"

class AvailabilityOverride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} on {self.date}: {'Available' if self.is_available else 'Unavailable'}"
