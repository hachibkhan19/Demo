from tabnanny import verbose
from django.db import models  
  
class Country(models.Model):  
    country = models.CharField(max_length=200, unique=True)  
    slug = models.CharField(max_length=200)
    iso2 = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "countries"
  
    def __str__(self):  
        return f'{self.country}' 
