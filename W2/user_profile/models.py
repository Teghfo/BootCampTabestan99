from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

import re
# from user_profile.models import Profile


class ProfileManager(models.Manager):
    def my_query(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from user_profile")
            res_list = []
            for i in cursor.fetchall():
                res_list.append(i)
        return res_list
    
    def truncate(self):
        from django.db import connection
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"TRUNCATE TABLE {self.model._meta.db_table} CASCADE")
            except Exception as e:
                raise e


class Profile(models.Model):
    gender_choices = [
        ('M', 'Male'), 
        ('F', 'Female')
    ]

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone_regx = r'^9\d{9}$'
    phone_regx = RegexValidator(regex=phone_regx, message='''shomare mobile ro 
                                                    dar format khaste shodeh vared nakardi: format dorost9xxxxxxxxx''')
    phone_number = models.CharField(validators=[phone_regx], max_length=50)
    address = models.CharField(max_length=500, default='')
    admin = models.CharField(max_length=20, blank=True, null= True)
    gender = models.CharField(max_length=1, null = True,choices=gender_choices)
    image = models.ImageField(uploa)
    objects = ProfileManager()

    class Meta:
        db_table = 'user_profile'

    def save(self, *args, **kwargs):
        phone_regx = r'^9\d{9}$'
        if not re.match(phone_regx, self.phone_number):
            raise '''khak tu saret'''
        
        super(Profile, self).save(*args, **kwargs)



# User.objects.bulk_create