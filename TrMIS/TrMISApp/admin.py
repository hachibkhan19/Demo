from pyexpat import model
from django.contrib import admin
from .models import Country

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country', 'slug', 'iso2')
    ordering = ('country',)

    class Meta:
        model = Country
        

admin.site.register(Country, CountryAdmin)
