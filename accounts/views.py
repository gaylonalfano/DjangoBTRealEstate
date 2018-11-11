from django.shortcuts import render, redirect
# Need to bring in the messages app
from django.contrib import messages


def register(request):
    # Determine if request is a GET or POST
    if request.method == 'POST':  # A form submission
        messages.error(request, "Testing error message")
        return redirect('register')
    else:  # Just render the form
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login User
        pass
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    # It won't render a template but instead redirect to index
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
