from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone_regx = r'9\d{9}'
    phone_regx = RegexValidator(phone_regx, message='''shomare mobile ro 
                                                    dar format khaste shodeh vared nakardi: format dorost9xxxxxxxxx''')
    phone_number = models.CharField(validators=[phone_regx], max_length=50)
    address = models.CharField(max_length=500, default='')

    class Meta:
        db_table = 'user_profile'