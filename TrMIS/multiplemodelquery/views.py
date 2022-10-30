from django.shortcuts import render, HttpResponse
from requests import request
from .models import Person

# Create your views here.
def home(request):
    perosn = Person.objects.all()
   

    print(perosn)

    return HttpResponse('multiplemodelquery')
