from dataclasses import fields
from random import choices
from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')
        



class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        # fields = '__all__'
        fields = ('id', 'pub_date', 'question_text', 'author', 'choice_set')

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        choice_set_serializer = self.fields['choice_set']
        for each in choice_validated_data:
            each['question'] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question
    
    
    