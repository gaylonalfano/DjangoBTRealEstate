from django.shortcuts import render, redirect


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # It won't render a template but instead redirect to index
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
