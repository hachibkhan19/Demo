from django.db import models  
  
class Book(models.Model):  
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    published_year = models.IntegerField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
  
    def __str__(self):  
        return f'{self.title}' 
