from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParentView.as_view())
]

