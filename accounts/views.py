from django.shortcuts import render, redirect
# Need to bring in the messages app
from django.contrib import messages, auth  # auth for login after registering
# Need to bring in Users
from django.contrib.auth.models import User


def register(request):
    # Determine if request is a GET or POST
    if request.method == 'POST':  # A form submission
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return redirect('register')
            # Check email
            elif User.objects.filter(email=email).exists():
                messages.error(request, "That email already exists")
                return redirect('register')
            else:
                # Looks good. Let's create the user
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                # Login after registering
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                messages.success(
                    request, "You are now registered and can log in")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:  # Just render the form
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # To be able to login/authenticate we need to create a variable called user
        # authenticate using whatever username and password submitted in form
        user = auth.authenticate(username=username, password=password)

        # If user is found
        if user is not None:
            # Login this user
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    # It won't render a template but instead redirect to index
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
