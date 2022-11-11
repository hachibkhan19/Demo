from email.policy import default
from enum import auto
from django.db import models
import datetime

class ParentModel(models.Model):
    parent_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.parent_name
    
    @property
    def year(self):
        return self.start_date.year
    
class ChildModel(models.Model):
    child_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.child_name
