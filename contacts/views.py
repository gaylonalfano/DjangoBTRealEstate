from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.


def contact(request):
    if request.method == 'POST':
        # Capture the fields
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Store all of these fields into a Contact object variable
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        # Save the object
        contact.save()

        # Display a message to the user that their request has been submitted
        messages.success(
            request, "Your request has been submitted, a realtor will contact you soon")

        # Redirect the user back to that listing page
        return redirect('/listings/'+listing_id)
