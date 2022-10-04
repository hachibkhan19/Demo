from django.shortcuts import render
from .filters import UserFilter
from django.contrib.auth.models import User

# def search(request):
#     user_list = User.objects.all()
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     print("user_filter ", user_filter)
#     return render(request, 'user_list.html', {"filter": user_filter})
