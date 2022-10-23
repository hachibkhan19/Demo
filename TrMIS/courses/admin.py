from django.contrib import admin
from .models import CourseCategory, Course, CourseDetails
# Register your models here.

admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(CourseDetails)



