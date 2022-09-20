from http import server
from django.shortcuts import render, HttpResponse
from .serializers import OrganizaionSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organizaion, Employee

# Create your views here.
# class OrganizaionAPIView(APIView):
#     def get(self,request):
#         organization = Organizaion.objects.all()
#         serializer = OrganizaionSerializer(organization, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class EmployeeAPIView(APIView):
    def get(self,request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)