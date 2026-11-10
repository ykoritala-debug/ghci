from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_helper = models.BooleanField(default=False)
    gender = models.CharField(max_length=10)
    certification_level = models.IntegerField(default=0)
    location = models.CharField(max_length=255)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    helper = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignments')
    tier = models.IntegerField(choices=[(1, 'Ride'), (2, 'Helper'), (3, 'Full Service')])
    status = models.CharField(max_length=20, default='pending')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    route = models.TextField()