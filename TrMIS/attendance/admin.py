from django.contrib import admin
from .models import ParentModel, ChildModel, Post

admin.site.register(ParentModel)
admin.site.register(ChildModel)
admin.site.register(Post)
