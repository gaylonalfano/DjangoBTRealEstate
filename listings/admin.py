from django.contrib import admin
from .models import Listing

# Documentation: https://docs.djangoproject.com/en/2.1/ref/contrib/admin/
# THIS WAS SECOND: We've already customized some of the Admin CSS. Now
# we want the Listings section within the Admin page to display more than
# just the standard address (i.e., title field). Need to create a class:


class ListingAdmin(admin.ModelAdmin):
    # We can add certain variables/properties that relate to how things are displayed
    # IMPORTANT: After creating this class, need to pass it to the
    # admin.site.register(Listing, ListingAdmin) below
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    # To enable another column field (i.e., "title") to be "clickable". Note that
    # the default clickable column is the FIRST column (so "id"):
    list_display_links = ('id', 'title')
    # To add a filter box for your realtors:
    list_filter = ('realtor',)  # Note the ","
    # To enable is_published to be a clickable checkbox:
    list_editable = ('is_published',)
    # To enable searching:
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    # Define/limit the number of listings to display per page:
    list_per_page = 25


# THIS WAS FIRST: Got the database up and going
# and migrated the Listing and Realtor classes. Also created
# a superuser account for admin.
# Now adding listings models to admin area:
admin.site.register(Listing, ListingAdmin)
