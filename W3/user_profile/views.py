from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Profile, Address

def signup(request):
    pass


def login(request):
    pass


def profile_show(request):
    if request.method == 'GET':
        user = User.objects.get(username = 'kasra')
        profile = Profile.objects.get(user = user)
        
        address = profile.address_by.all() 

        return render(request, 'profile.html', {'profile': profile, 'address': address})  


def edit_profile(request):
    pass
