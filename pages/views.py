from django.shortcuts import render
from django.http import HttpResponse
# Bringing in Listing model from listings app models to make the home page dynamic
from listings.models import Listing
# Time to bring in Realtor model from realtors app models to make about page dynamic
from realtors.models import Realtor
# Import the Python dicts that are storing search form options (states, price, bedrooms, etc)
from listings.choices import price_choices, state_choices, bedroom_choices

# Create method/function called index so that our 'index' path can access use it


def index(request):
    # We're wanting to pull three listings in desc order and only published
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    # Add search form choices to context
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    # We want ot render a template for the home page. For now we just bring in
    # a HttpResponse
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP (or MVPs if they want multiple)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
