from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(Common, AbstractUser):
    TYPE_CHOICES = (
        ('INDIVIDUAL', 'Individual'),
        ("ENTERPRISE", "Enterprise"),
        ("GOVERNMENT", "Government"),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    username = models.CharField(max_length=30, unique=True, null=False)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    user_email = models.EmailField(null=True)
    address = models.CharField(max_length=500, null=True)
    pincode = models.IntegerField(null=True)
    country = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    country_code = models.CharField(max_length=10, null=True, 
                    help_text=_('Optional: country code format +91'))
    user_phone_no = models.CharField(max_length=20, null=True, 
                    help_text=_('Optional: phone number format 8130514811.'))
    password = models.CharField(_('Password'), max_length=155, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

class Incident(Common, models.Model):
    PRIORITY_CHOICES = (
        ('HIGH', 'High'),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
    )
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ("IN PROGRESS", "In Progress"),
        ("CLOSED", "Closed"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    incident_id = models.CharField(max_length=20, null=True)
    incident_details = models.TextField(null=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=20, null=True)
    incident_status = models.CharField(choices=STATUS_CHOICES, max_length=20, 
                                        null=True, default='OPEN')