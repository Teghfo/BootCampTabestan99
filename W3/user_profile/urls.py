from django.urls import path

from .views import signup, login, profile_show, edit_profile

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', login, name = 'log-in'),
    path('profile/', profile_show , name = 'profile'),
    path('profile/edit', edit_profile,  name = 'edit-profile'),
]