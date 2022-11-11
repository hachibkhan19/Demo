from django.contrib import admin
from .models import Question, OptionGroup, Option

# Register your models here.
admin.site.register(Question)
admin.site.register(OptionGroup)
admin.site.register(Option)
