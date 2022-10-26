from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

class Comment(models.Model):
    comment_content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_rel')
    
    def __str__(self):
        return self.comment_content
        