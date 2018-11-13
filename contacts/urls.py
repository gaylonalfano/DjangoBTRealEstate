# In this file we're only going to have one URL for the submission
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact')
]
