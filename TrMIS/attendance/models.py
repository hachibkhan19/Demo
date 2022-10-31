from django.db import models

class ParentModel(models.Model):
    parent_name = models.CharField(max_length=200)

class ChildModel(models.Model):
    child_name = models.CharField(max_length=200)
    