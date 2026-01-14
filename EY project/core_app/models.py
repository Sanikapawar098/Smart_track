from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_society_manager = models.BooleanField(default=False)
    is_citizen = models.BooleanField(default=True)


class CitizenProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='citizenprofile')
    area_address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"


class Citizen(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    area = models.TextField(blank=True)
    lane_number = models.IntegerField()

    def __str__(self):
        return self.name


class Complaint(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_WORKING = 'working'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_WORKING, 'Working'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    complaintDate = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return f"Complaint #{self.pk} by {self.customer.username} - {self.status}"
