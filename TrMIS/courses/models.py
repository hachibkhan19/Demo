from email.policy import default
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.utils import timezone

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

class CourseDetails(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='course_details_id')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column="course_id")
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    class Meta:
        db_table = 'course_details'
        
    def __str__(self):
        return self.course.name

class CurrentDate(models.Model):
    name= models.CharField(max_length=150)
    currentdate= models.DateField(default=timezone.now)