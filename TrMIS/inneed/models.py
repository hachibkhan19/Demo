from django.db import models

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=1000, blank=False, default='')

    def __str__(self):
        return self.content

class OptionGroup(models.Model):

    question = models.ForeignKey('Question', on_delete=models.CASCADE, default='')

    options = models.ManyToManyField('Option')


class Option(models.Model):

    content = models.CharField(max_length=1000, blank=False, default='')

