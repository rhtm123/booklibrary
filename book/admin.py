from django.contrib import admin

# Register your models here.

from book.models import Book, Publisher, BookAuthor


admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookAuthor)
