from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Now e've setup the database, added some listings data, configured the admin area
# **IMPORTANT** The idea here is to fetch our listings using our model and then we
# insert it into our template, and then we can simply loop through and output the
# listings that are in the database! In order to do that we need to bring in any
# model we want into any file we want and use it! In this case we want to bring in
# our Listing model using from .models import Listing
from .models import Listing
# Import the Python dicts that are storing search form options (states, price, bedrooms, etc)
from .choices import price_choices, state_choices, bedroom_choices

# Already created the paths for listings, listing, and search
# They use views methods we need to create:
# index() is main listings page:


def index(request):
    """view we want to render fetch listings from database"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # create a dict to store listings we want to pass to the template
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Need to pass listing_id parameter (above)"""
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    """Similar to our pages index method to handle the search form"""
    # Build our search form queryset
    queryset_list = Listing.objects.order_by('-list_date')

    # Building our filters
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    # Add search form choices to context
    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        # Adding 'values' to context to preserve search criteria
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
