from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    ordering = ('title',)

    class Meta:
        model = Book
        

admin.site.register(Book, BookAdmin)
