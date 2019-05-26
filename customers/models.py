from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    is_master = models.BooleanField(default=False, help_text='Make as master')
    phone = models.CharField(max_length=254, null=True, blank=True)

    # output object info
    def __str__(self):
        return self.email
