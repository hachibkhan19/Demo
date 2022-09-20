from http import server
from django.shortcuts import render, HttpResponse
from .serializers import OrganizaionSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organizaion, Employee
from rest_framework import generics

# Create your views here.
# class OrganizaionAPIView(APIView):
#     def get(self,request):
#         organization = Organizaion.objects.all()
#         serializer = OrganizaionSerializer(organization, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer