
from django.urls import path
from Appone import views

urlpatterns = [
    path('home', views.home, name='home'),  # Add your app's home view
]