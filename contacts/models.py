from django.db import models
from datetime import datetime


class Contact(models.Model):
    # Fields we're going to have for Contact object
    # Don't need a relationship between Contact and Listing
    # We just need Listing Title and ID
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)  # Longer text, Optional
    contact_date = models.DateTimeField(
        default=datetime.now, blank=True)  # Optional
    # Will be connected to whatever registered user is logged in. Optional for Guests
    user_id = models.IntegerField(blank=True)

    # Create a __str__ method to represent the object. Use 'name' to represent.
    def __str__(self):
        return self.name
