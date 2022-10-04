from email.policy import default
from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from requests import delete


class BaseModel(models.Model):
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseSoftDeleteTableModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def soft_delete(self, user_id=None):
        self.is_deleted = True
        self.deleted_by = user_id
        self.deleted_at = timezone.now()
        self.save()


class Address(BaseModel, BaseSoftDeleteTableModel):
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.country

