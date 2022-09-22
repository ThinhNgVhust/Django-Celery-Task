from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# celery
from myapp.tasks import add


 # Create your views here.

def index(request):
    add.delay(5,10)
    return HttpResponse("Hello, world!")