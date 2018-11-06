from django.contrib import admin
from .models import Listing

# Register your models here.
# THIS WAS SECOND: We've already customized some of the Admin CSS. Now
# we want the Listings section within the Admin page to display more than
# just the standard address (i.e., title field). Need to create a class:


class ListingAdmin(admin.ModelAdmin):
    # We can add certain variables/properties that relate to how things are displayed
    # IMPORTANT: After creating this class, need to pass it to the
    # admin.site.register(Listing, ListingAdmin) below
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')


# THIS WAS FIRST: Got the database up and going
# and migrated the Listing and Realtor classes. Also created
# a superuser account for admin.
# Now adding listings models to admin area:
admin.site.register(Listing, ListingAdmin)
