from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe


# Create your models here.
class Users(AbstractUser):
    staff_id = models.TextField(max_length=50, unique=True, default='NIT/Staff/1')
    transport = models.BooleanField(default=False)
    driver = models.BooleanField(default=False)
    humanresource = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    workshop = models.BooleanField(default=False)
    gpsa = models.BooleanField(default=False)

    USERNAME_FIELD = 'staff_id'
