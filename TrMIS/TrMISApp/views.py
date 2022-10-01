from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Book
# import requests
# from .serializers import CountrySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def home(request):
    queryset = Book.objects.all()
    if queryset.exists() == False:
        Book.objects.bulk_create([

            Book(title='Python Crash Course, 2nd Edition', author='Eric Matthes', price=15, published_year=2019),

            Book(title='Automate the Boring Stuff with Python, 2nd Edition', author='Al Sweigart', price=30, published_year=2019),

            Book(title='Learning Python', author='Mark Lutz', price=15, published_year=2019),

            Book(title='Head First Python', author='Paul Barry', price=45, published_year=2016),

            Book(title='A Byte of Python', author='Swaroop C H', price=15, published_year=2013),


        ])

    return HttpResponse('hi')

   
