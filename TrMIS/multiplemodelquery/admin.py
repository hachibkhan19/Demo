from django.contrib import admin
from .models import Person, Appointment, Sales
# Register your models here.
admin.site.register(Person)
admin.site.register(Appointment)
admin.site.register(Sales)
