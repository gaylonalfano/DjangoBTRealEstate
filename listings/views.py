from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Now e've setup the database, added some listings data, configured the admin area
# **IMPORTANT** The idea here is to fetch our listings using our model and then we
# insert it into our template, and then we can simply loop through and output the
# listings that are in the database! In order to do that we need to bring in any
# model we want into any file we want and use it! In this case we want to bring in
# our Listing model using from .models import Listing
from .models import Listing

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
    return render(request, 'listings/listing.html')


def search(request):
    """Haven't updated"""
    return render(request, 'listings/search.html')
