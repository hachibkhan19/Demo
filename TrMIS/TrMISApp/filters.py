from dataclasses import fields
from django.contrib.auth.models import User, Group, GroupManager
import django_filters

class UserFilter(django_filters.FilterSet):
    # first_name = django_filters.CharFilter(lookup_expr='icontains')
    # year_joined = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year')
    # year_joined__gt = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year_gt')
    # year_joined__lt = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year_lt')

    first_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())
    
    class Meta:
        model = User
        # fields = {
        #     'username':['exact', ],
        #     'first_name': ['icontains', ], 
        #     'last_name': ['exact', ],
        #     'date_joined': ['year', 'year__gt', 'year__lt']

        #     }
        fields = ('username' , 'first_name', 'last_name', 'year_joined', 'groups')
