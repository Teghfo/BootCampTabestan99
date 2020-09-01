from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello),
    path('bye', views.goodbye),

]
