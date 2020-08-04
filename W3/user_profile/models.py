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
    '''
    cinema_ticket member's Profile.
    using User model of django for generaing user profile.

     
    '''
    gender_choices = [
        ('M', 'Male'), 
        ('F', 'Female')
    ]

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone_regx = r'^9\d{9}$'
    phone_regx = RegexValidator(regex=phone_regx, message='''shomare mobile ro 
                                                    dar format khaste shodeh vared nakardi: format dorost9xxxxxxxxx''')
    phone_number = models.CharField(validators=[phone_regx], max_length=50)
    admin = models.CharField(max_length=20, blank=True, null= True)
    gender = models.CharField(max_length=1, null = True,choices=gender_choices)
    verified_account = models.BooleanField(default=False)
    objects = ProfileManager()

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        phone_regx = r'^9\d{9}$'
        if not re.match(phone_regx, self.phone_number):
            raise '''khak tu saret'''
        
        super(Profile, self).save(*args, **kwargs)



CITY_CHOICE = [
    ('tehran', 'Tehran'),
    ('shiraz', 'Shiraz'),
    ('tabriz', 'Tabriz')
]

class Address(models.Model):
    '''
    every user can have multiple address for sending receiving ticket!


    '''
    profile = models.ForeignKey(Profile, related_name = 'address_by', on_delete = models.CASCADE)
    city = models.CharField('شهر', max_length=10 , help_text='شهر', choices=CITY_CHOICE)
    add = models.CharField('آدرس', max_length=50, null = True)

    def __str__(self):
        return f"{self.profile.user}-{self.id}"
# User.objects.bulk_create