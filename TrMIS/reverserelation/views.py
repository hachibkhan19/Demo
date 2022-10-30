from django.shortcuts import render, HttpResponse
from requests import request
from .models import Post

# Create your views here.
def home(request):
    post = Post.objects.filter(comments_rel__comment_content='comment-2')
    print(post)
    return HttpResponse('Hi')
