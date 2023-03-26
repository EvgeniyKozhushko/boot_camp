from django.contrib import admin

# Register your models here.

from . import models



class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title_book', 'date_inclusion']
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'author_discription']

admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)