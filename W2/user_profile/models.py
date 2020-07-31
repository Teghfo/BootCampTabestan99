from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=500, default='')

    class Meta:
        db_table = 'user_profile'