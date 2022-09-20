from urllib import response
# from django.http import HttpResponse
from django.shortcuts import render
from .models import Category

# Views are Python functions that receive an HttpRequest object and returns an HttpResponse object. 
# Receive a request as a parameter and returns a response as a result. 
# That’s the flow you have to keep in mind!

# Now we have to tell Django when to serve this view. It’s done inside the urls.py file:
def home(request):
  categories = Category.objects.all()
  
  return render(request, 'home.html', {'categories': categories})
  # return HttpResponse(response_html)