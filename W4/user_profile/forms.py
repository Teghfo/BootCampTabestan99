from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['phone_number', 'gender']
        labels = {
            'phone_number': 'شماره تلفن',
            'gender': 'جنسیت'
        }
