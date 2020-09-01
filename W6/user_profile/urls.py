from django.urls import path

from .views import register, custom_login, custom_logout, profile_show, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login, name='log-in'),
    path('logout/', custom_logout, name='log-out'),
    path('profile/', profile_show, name='profile'),
    path('profile/edit', edit_profile,  name='edit-profile'),
]
