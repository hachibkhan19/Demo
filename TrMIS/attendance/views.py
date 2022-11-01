from http import server
from django.shortcuts import render, HttpResponse
from .serializers import ParentModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ParentModel
from rest_framework import generics

from django.shortcuts import render, get_object_or_404
from .models import Post

class ParentView(APIView):
    def get(self, request):
        parent = ParentModel.objects.all()
        serializer = ParentModelSerializer(parent, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




def detail_post_view(request, id=None):
        postobj= get_object_or_404(Post, id=id)

        context={'postobj': postobj}
        

        return render (request, 'posts/detail.html', context)