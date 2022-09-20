from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeAPIView.as_view())
]
