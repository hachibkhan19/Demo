from re import template
from unicodedata import name
from django.urls import path
from . import views
from django_filters.views import FilterView
from .filters import UserFilter

urlpatterns = [
    path('', FilterView.as_view(filterset_class=UserFilter, template_name='user_list.html'), name='search'),
]
