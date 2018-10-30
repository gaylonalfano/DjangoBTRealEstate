"""btre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
* **PROCESS OVERVIEW**: For this example we’re going to add an about page to our blog app: blog > urls.py > urlpatterns: path(‘about/', views.about, name=‘blog-about’). **NOTE: This is a little different than the process overview above since the one above is add adding a route to the main project! For this example, we’re only adding a new route/path within the blog app. This is a key difference and aligns with the Django framework and adding multiple apps within the site (i.e., a blog app in this case). It wants to keep the blog-specific (app-specific) functionality to be separate from the project-level functionality. So, if a user requests a page that’s within the blog app, the project will redirect the request to the blog app urls.py to be further handled.
    * If a user/visitor to our site goes to the blog/about page, the request will now reference/be sent over to our blog.urls
    * When Django encounters include(), it chops off the included portion of the url (“blog/") and only sends the remaining string (“about/" in this case) to the included blog.urls module to get processed. Since “about/" is remaining, it just sends the string “about/" over to blog.urls. 
    * Once it’s passed over to blog.urls, Django then starts searching for a matching “about/” string. Essentially Django is asking, "Do I have a pattern in here that matches “about/”?" Turns out yes we do: urlpatterns: path(‘about/', views.about, name=‘blog-about’)
    * Based on the urlpattern, the “about/” route will be handled by the function views.about (defined in blog views.py): def about(request): return HttpResponse(‘<h1>Blog About</h1>’).
    * So then we can navigate to our views.py file and then find the home function. Now it/the request comes to this home function and executes (the home function takes request as an argument).  
    * In this example, the home function essentially runs/says, "Ok, so now we just want to return an HttpResponse with an <h1> that says "Blog Home"." That's the whole process basically.
* **IMPORTANT**: Why it’s good that the URL gets passed around like this:  If we wanted to change the route to our blog application (or any app we build for that matter), then we can change the URL in one place and it applies to all of those routes! For example, say we are building a blog that’s in development and we want to do some live testing on our website but weren’t ready to make it fully live just yet. We could simply go to our project urls.py urlpatterns and change the path from ‘blog/‘ to ‘blog_dev/‘ - it’s that easy! With that one change, in order to go to my blog that I’m developing and testing on my site, I just have to enter …/blog_dev/ and all the links/urls within the blog application will still be accessible through this blog_dev/ route now! Didn’t have to change anything in our blog application. Only had to change the one project path in the urls.py urlpatterns!

"""


from django.contrib import admin
# Need to import include() from django.urls so you can link the path to the
# urls.py file inside the pages app:
from django.urls import path, include

urlpatterns = [
    # if you want to go straight to home page then use ''
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
