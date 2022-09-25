from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_view),
    path('country/', views.country),
]
