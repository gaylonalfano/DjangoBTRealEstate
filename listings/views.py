from django.shortcuts import render

# Already created the paths for listings, listing, and search
# They use views methods we need to create:
# index() is main listings page:


def index(request):
    # view we want to render
    render(request, 'listings/listings.html')


def listing(request):
    render(request, 'listings/listing.html')


def search(request):
    render(request, 'listings/search.html')
