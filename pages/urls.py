# Idea here is to have a url/path/route that is attached to a method
# that's inside the views.py file. We want a url for the home page
from django.urls import path
from . import views

urlpatterns = [
    # home page route/path (root path, method we want to connect to in the views, name to access the path)
    path('', views.index, name='index')
]