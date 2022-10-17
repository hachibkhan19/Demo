from django import views
from django.urls import path
from .views import home

app_name = 'date_time_Field'
urlpatterns = [
    path('', home, name='home')

]
