from django.db import models
from django.contrib.auth.models import User

from uuid import uuid4

ORDER_STATUS = [
    (),
]


class Order(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'order')
    
    date_created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length= 10, choices=ORDER_STATUS)