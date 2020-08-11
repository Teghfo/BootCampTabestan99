from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Address


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email',
                  'is_staff', 'password1', 'password2']


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})

    form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        if authenticate(username=username, password=password):
            user_obj = User.objects.get(username=username)
            login(request, user_obj)
            return redirect("home")
        else:
            return render(request, 'login.html')

        print(request.POST)
    return render(request, 'login.html')


def profile_show(request):
    if request.method == 'GET':
        user = User.objects.get(username='kasra')
        profile = Profile.objects.get(user=user)

        address = profile.address_by.all()

        return render(request, 'profile.html', {'profile': profile, 'address': address})


def custom_logout(request):
    logout(request)
    return redirect('home')


def edit_profile(request):
    pass
