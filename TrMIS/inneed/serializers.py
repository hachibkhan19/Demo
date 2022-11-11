from rest_framework import serializers
from .models import Option, OptionGroup, Question

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('content',)

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('content', 'options')