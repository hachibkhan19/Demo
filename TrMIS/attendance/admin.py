from django.contrib import admin
from .models import ParentModel, ChildModel

admin.site.register(ParentModel)
admin.site.register(ChildModel)
