from http import server
from django.shortcuts import render, HttpResponse
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question 
from rest_framework import generics



class QuestionView(APIView):
    def get(self, request):
        question = Question.objects.prefetch_related('choices')
        # question = Question.objects.select_related('choices').all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

