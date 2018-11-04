from django.contrib import admin
from .models import Listing

# Register your models here. Got the database up and going
# and migrated the Listing and Realtor classes. Also created
# a superuser account for admin. Now adding listings models to
# admin area:
admin.site.register(Listing)
