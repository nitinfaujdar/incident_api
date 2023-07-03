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

    username = models.CharField(max_length=30, unique=True, null=False)
    user_email = models.EmailField(_('email_address'), null=True, blank=True)
    user_phone_no = models.CharField(
        _('phone'), max_length=20, blank=True, null=True, help_text=_('Optional: phone number format +918130514811.'),
        db_index=True
    )
    password = models.CharField(_('Password'), max_length=155, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
