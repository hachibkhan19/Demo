from email.policy import default
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date


# Create your models here.
class CourseCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column="course_category_id")
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'course_category'


    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True, db_column='course_id')
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, db_column="course_category_id")
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name

def no_small_date(value):
    today = date.today() 
    if value < today: 
            raise ValidationError('End Date cannot be small in from course create date.') 

class CourseDetails(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='course_details_id')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column="course_id")
    start_at = models.DateField(help_text="Please enter today's date")
    end_at = models.DateField(help_text="Please enter end date", validators = [no_small_date])

    class Meta:
        db_table = 'course_details'
        
    def __str__(self):
        return self.course.name
