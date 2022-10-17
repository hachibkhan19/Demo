from django.core.exceptions import ValidationError
from datetime import date
from django.db import models

def no_future(value):
    today = date.today() 
    if value > today: 
            raise ValidationError('Purchase Date cannot be in the future.') 

class Member_Registration(models.Model): 
        Purchase_Date = models.DateField(help_text = "Enter the date of purchase", validators = [no_future])