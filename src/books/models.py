from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=60)
    author_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)

    def __str__(self) -> str:
        return f'Автор {self.name}'

    def get_absolute_url(self):
        return reverse('home-authors')    

class Book(models.Model):
    title_book = models.CharField(verbose_name="Название книги", max_length= 200)
    book_author = models.ManyToManyField(Author, default='Автор', related_name='authors') # должен быть справочник
    book_series = models.CharField(verbose_name="Серия книг", max_length= 50)
    book_genre = models.CharField(verbose_name="Жанр", max_length= 20)
    year_publishing = models.IntegerField(verbose_name= "Год издания")
    number_pages = models.IntegerField(verbose_name="Количество страниц")
    size = models.CharField(verbose_name="Формат", max_length= 100)
    ISBN = models.CharField(verbose_name="ISBN",max_length= 100)
    publishing_house = models.CharField(verbose_name="Издательство", max_length= 40)
    rating = models.IntegerField(verbose_name="Рейтинг (0-10)", blank=True, null=True)
    date_inclusion = models.DateTimeField(verbose_name="Дата внесения в каталог", auto_now_add=True, auto_now=False)
    date_change = models.DateTimeField(verbose_name="Дата последнего изменения карточки", auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return f"{self.title_book}"

    def get_absolute_url(self):
        return reverse('home-books')        