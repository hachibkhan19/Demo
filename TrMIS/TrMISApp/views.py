from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Country
import requests
from .serializers import CountrySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def country_view(request):
    response = requests.get("https://api.covid19api.com/countries")
    datas = response.json()
    for data in datas:
        # print(data)
        country_data = Country(country= data['Country'], slug= data['Slug'], iso2= data['ISO2'])
        country_data.save()
        # print(data['Country'])
    return HttpResponse('hi')
    

@api_view(['GET'])
def country(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
