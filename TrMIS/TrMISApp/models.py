from django.db import models

# Create your models here.
class Organizaion(models.Model):
    organization_name = models.CharField(max_length=200, verbose_name='organization name')
    address = models.CharField(max_length=200, verbose_name='organization address', default='')
    type = models.CharField(max_length=200, verbose_name='organization type', default='')

    def __str__(self):
        return self.organization_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=200, verbose_name='employee name')
    employee_address = models.CharField(max_length=200, verbose_name='employee address')
    age = models.IntegerField()
    organization_type = models.ForeignKey(Organizaion, on_delete=models.CASCADE)
    def __str__(self):
        return self.employee_name