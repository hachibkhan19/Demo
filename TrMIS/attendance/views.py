from http import server
from django.shortcuts import render, HttpResponse
from .serializers import ParentModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ParentModel
from rest_framework import generics



class ParentView(APIView):
    def get(self, request):
        parent = ParentModel.objects.all()
        serializer = ParentModelSerializer(parent, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)