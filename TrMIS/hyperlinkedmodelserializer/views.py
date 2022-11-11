from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import InNeedSerializer
from .models import InNeed
  

class InNeedViewSet(viewsets.ModelViewSet):
    queryset = InNeed.objects.all()
    serializer_class = InNeedSerializer
    http_method_names = ['get', 'post']