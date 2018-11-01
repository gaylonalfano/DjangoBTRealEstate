# Idea here is to have a url/path/route that is attached to a method
# that's inside the views.py file. We want a url for the home page
from django.urls import path
from . import views

# If we left the path('') empty, this pertains to the /listings url, so we want this path
# to call index method INSIDE of the listings views file, so we'll change the name from 'index'
# to instead be 'listings'
urlpatterns = [
    # /listings route/path (root path, method we want to connect to in the views, name to access the path)
    path('', views.index, name='listings'),
    # After creating the templates created need to create path for SINGLE listings,
    # we want it to look like: /listings/23 (ID number)
    path('<int:listing_id>/', views.listing, name='listing'),
    # Create a path for search. It'll go to a method called search. Only need 'search/' (instead of listings/search)
    # since we're going to link it to the main urls.py and tell it that anything that has 'listings/' should
    # look at this file (we're basically using the include() method)
    path('search', views.search, name='search')
]
