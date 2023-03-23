from django.contrib import admin

# Register your models here.

from . import models

# class BookAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'title_book', 'author', 'date_inclusion']

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title_book', 'date_inclusion']

admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author)