from email.policy import default
from enum import auto
from django.db import models
import datetime

class ParentModel(models.Model):
    parent_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.parent_name
    
    @property
    def year(self):
        return self.start_date.year
    
class ChildModel(models.Model):
    child_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.child_name



from django.template.defaultfilters import slugify


class Post(models.Model):
    title= models.CharField(max_length=300)
    url= models.SlugField(max_length=300)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def yearpublished(self):
        return self.pub_date.strftime('%Y')


