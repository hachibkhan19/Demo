from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Organizaion, Employee

class OrganizaionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizaion
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    org_type= serializers.ReadOnlyField(source='organization_type.organization_name')

    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'employee_address', 'age', 'organization_type', 'org_type')
    