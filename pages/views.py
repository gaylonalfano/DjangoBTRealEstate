from django.shortcuts import render
from django.http import HttpResponse

# Create method/function called index so that our 'index' path can access use it


def index(request):
    # We want ot render a template for the home page. For now we just bring in
    # a HttpResponse
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
