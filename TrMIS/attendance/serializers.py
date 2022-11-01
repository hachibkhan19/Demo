from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import ParentModel, ChildModel
from . import models


class ChildModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.ChildModel
        fields = "__all__"

class ParentModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    child = serializers.SerializerMethodField()

    class Meta:
        model = models.ParentModel

        fields = ("id", "parent_name", "year", "child")

    def get_child(self, obj):
        child = models.ChildModel.objects.all()
        return ChildModelSerializer(child, many=True).data
